/**
 * Academic Examination Engine
 * Al Rehman Public Secondary School Sadwal (Chakwal)
 * Principal: Dr. Shaukat Aziz
 */

const SCHOOL_CONFIG = {
  name: "Al Rehman Public Secondary School Sadwal",
  fullName: "Al Rehman Public Secondary School Sadwal (Chakwal)",
  campus: "Sadwal, Tehsil & District Chakwal",
  motto: "Enter to Learn - Leave to Serve",
  session: "2026-27",
  examTitle: "2nd Term Examination 2026-27",
  principal: "Dr. Shaukat Aziz"
};

const GRADING_SCALE = [
  { minPct: 90.0, maxPct: 100.0, grade: "A+", remarks: "Excellent", badgeClass: "bg-emerald-100 text-emerald-800 border-emerald-300 ring-1 ring-emerald-300" },
  { minPct: 80.0, maxPct: 90.0,  grade: "A",  remarks: "Very Good", badgeClass: "bg-blue-100 text-blue-800 border-blue-300 ring-1 ring-blue-300" },
  { minPct: 70.0, maxPct: 80.0,  grade: "B",  remarks: "Good",      badgeClass: "bg-sky-100 text-sky-800 border-sky-300 ring-1 ring-sky-300" },
  { minPct: 60.0, maxPct: 70.0,  grade: "C",  remarks: "Satisfactory", badgeClass: "bg-amber-100 text-amber-800 border-amber-300 ring-1 ring-amber-300" },
  { minPct: 50.0, maxPct: 60.0,  grade: "D",  remarks: "Work Hard", badgeClass: "bg-orange-100 text-orange-800 border-orange-300 ring-1 ring-orange-300" },
  { minPct: 40.0, maxPct: 50.0,  grade: "E",  remarks: "Poor",      badgeClass: "bg-purple-100 text-purple-800 border-purple-300 ring-1 ring-purple-300" },
  { minPct: 0.0,  maxPct: 40.0,  grade: "F",  remarks: "Fail",      badgeClass: "bg-rose-100 text-rose-800 border-rose-300 ring-1 ring-rose-300" }
];

function getOrdinal(n) {
  const s = ["th", "st", "nd", "rd"];
  const v = n % 100;
  return n + (s[(v - 20) % 10] || s[v] || s[0]);
}

function resolvePassRate(classMeta) {
  if (classMeta.passRate) return classMeta.passRate;
  const name = (classMeta.className || "") + " " + (classMeta.section || "");
  if (/section\s*a/i.test(name)) return 0.70;
  return 0.40; // 40% default for Boys, Girls, Section B
}

/**
 * Process entire class dataset:
 * Supports dictionary structure where students are keyed by Student Name,
 * and marks are stored in key-value pairs (subjectName: mark).
 */
function processClass(classData, passRateOverride = null) {
  const passRate = passRateOverride !== null ? passRateOverride : resolvePassRate(classData.meta);
  
  // Normalize subjects list
  const subjectList = Object.entries(classData.subjects).map(([title, maxMarks]) => ({
    title: title,
    maxMarks: maxMarks
  }));

  const totalMax = subjectList.reduce((sum, s) => sum + s.maxMarks, 0);

  // Process all students from dictionary
  const processed = Object.entries(classData.students).map(([studentName, data]) => {
    // Handle SLC (School Leaving Certificate)
    if (data.status === 'SLC' || data.isSLC) {
      return {
        sr: data.rollNo,
        rollNo: data.rollNo,
        name: studentName,
        isSLC: true,
        status: 'SLC',
        subjectResults: subjectList.map(sub => ({
          title: sub.title,
          maxMarks: sub.maxMarks,
          passingMin: Math.ceil(sub.maxMarks * passRate),
          mark: '-',
          isPass: false
        })),
        rawTotal: 0,
        validTotal: 0,
        excludedMarks: 0,
        failedSubjects: [],
        hasFailedSubject: false,
        totalMax: totalMax,
        percentage: 0,
        grade: 'SLC',
        remarks: 'School Leaving Certificate',
        badgeClass: 'bg-slate-100 text-slate-500 border-slate-300',
        attendance: data.attendance !== undefined ? String(data.attendance) : '-',
        position: '-'
      };
    }

    let rawTotal = 0;
    let validTotal = 0;
    let failedSubjects = [];
    let subjectResults = [];

    subjectList.forEach(sub => {
      const val = data.marks[sub.title];
      const isNumeric = typeof val === 'number' && !isNaN(val);
      const numVal = isNumeric ? val : 0;
      const mark = val !== undefined ? val : '-';
      const passingMin = Math.ceil(sub.maxMarks * passRate);
      const isPass = isNumeric && numVal >= passingMin;

      rawTotal += numVal;
      if (isPass) {
        validTotal += numVal;
      } else {
        failedSubjects.push({
          title: sub.title,
          mark: mark,
          maxMarks: sub.maxMarks,
          passingMin: passingMin
        });
      }

      subjectResults.push({
        title: sub.title,
        maxMarks: sub.maxMarks,
        passingMin: passingMin,
        mark: mark,
        isPass: isPass
      });
    });

    const percentage = parseFloat(((validTotal / totalMax) * 100).toFixed(2));

    let grade = "F";
    let remarks = "Fail";
    let badgeClass = "bg-rose-100 text-rose-800 border-rose-300";

    for (const crit of GRADING_SCALE) {
      if (crit.grade === "A+" && percentage > 90.0) {
        grade = crit.grade;
        remarks = crit.remarks;
        badgeClass = crit.badgeClass;
        break;
      } else if (percentage > crit.minPct && percentage <= crit.maxPct) {
        grade = crit.grade;
        remarks = crit.remarks;
        badgeClass = crit.badgeClass;
        break;
      } else if (crit.grade === "F" && percentage < 40.0) {
        grade = crit.grade;
        remarks = crit.remarks;
        badgeClass = crit.badgeClass;
        break;
      }
    }

    return {
      sr: data.rollNo,
      rollNo: data.rollNo,
      name: studentName,
      isSLC: false,
      status: 'Active',
      subjectResults: subjectResults,
      rawTotal: rawTotal,
      validTotal: validTotal,
      excludedMarks: rawTotal - validTotal,
      failedSubjects: failedSubjects,
      hasFailedSubject: failedSubjects.length > 0,
      totalMax: totalMax,
      percentage: percentage,
      grade: grade,
      remarks: remarks,
      badgeClass: badgeClass,
      attendance: data.attendance !== undefined ? String(data.attendance) : '',
      position: 0
    };
  });

  // Assign positions by validTotal desc (active students only)
  const activeStudents = processed.filter(s => !s.isSLC);
  const sorted = [...activeStudents].sort((a, b) => b.validTotal - a.validTotal);
  sorted.forEach((st, idx) => {
    st.position = idx + 1;
  });

  // Re-sort by Roll No
  processed.sort((a, b) => a.rollNo - b.rollNo);

  const totalObtainedSum = activeStudents.reduce((sum, s) => sum + s.validTotal, 0);
  const classAvgPct = activeStudents.length > 0 ? (totalObtainedSum / (activeStudents.length * totalMax) * 100).toFixed(2) : "0.00";
  const topStudent = sorted[0];
  const failedStudents = activeStudents.filter(s => s.hasFailedSubject);

  return {
    meta: {
      ...classData.meta,
      passRate: passRate,
      passPercentLabel: Math.round(passRate * 100) + "%",
      totalMaxMarks: totalMax,
      enrolledCount: processed.length,
      activeCount: activeStudents.length,
      slcCount: processed.length - activeStudents.length,
      classAveragePct: classAvgPct,
      topStudent: topStudent,
      failedStudentsCount: failedStudents.length,
      principal: classData.meta.principal || SCHOOL_CONFIG.principal
    },
    subjects: subjectList,
    students: processed,
    failedStudents: failedStudents
  };
}

if (typeof module !== 'undefined') {
  module.exports = {
    SCHOOL_CONFIG,
    GRADING_SCALE,
    getOrdinal,
    resolvePassRate,
    processClass
  };
}
