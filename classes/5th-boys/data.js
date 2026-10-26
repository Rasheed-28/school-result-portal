/**
 * Academic Dataset: 5th Boys
 * Examination: 2nd Term 2026-27
 * Incharge: Farzana Parveen
 * Principal: Dr. Shaukat Aziz
 * 
 * Source: Official 2nd Term Mark Sheet (Sadwal Campus)
 * Master copy of 5th Boys dataset.
 */

const CLASS_DATA = {
  meta: {
    id: "5th_boys",
    className: "5th",
    section: "Boys",
    fullName: "5th Boys",
    session: "2026-27",
    term: "2nd Term Examination",
    incharge: "Farzana Parveen",
    principal: "Dr. Shaukat Aziz",
    date: "October 2026",
    passRate: 0.40 // 40% passing standard for Boys Section
  },
  // Subjects and their maximum marks (Total: 290)
  subjects: {
    "English": 50,
    "Urdu": 50,
    "Mathematics": 50,
    "General Science": 50,
    "Computer": 10,
    "Social Studies": 30,
    "Islamiat": 20,
    "Drawing": 10,
    "Al-Quran": 10,
    "Oral Assessment": 10
  },
  // Student Name as Object Key with Subject Marks as Key-Value Pairs
  students: {
    "Muhammad Shehrar": {
      rollNo: 1,
      marks: {
        "English": 49,
        "Urdu": 46,
        "Mathematics": 49,
        "General Science": 48,
        "Computer": 10,
        "Social Studies": 29,
        "Islamiat": 20,
        "Drawing": 7,
        "Al-Quran": 9,
        "Oral Assessment": 10
      }
    },
    "Muhammad Abdullah": {
      rollNo: 2,
      marks: {
        "English": 49,
        "Urdu": 44,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 7,
        "Al-Quran": 10,
        "Oral Assessment": 10
      }
    },
    "Kashan Ahmed": {
      rollNo: 3,
      marks: {
        "English": 49,
        "Urdu": 44,
        "Mathematics": 50,
        "General Science": 49,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 4,
        "Al-Quran": 7,
        "Oral Assessment": 10
      }
    },
    "Muhammad Haris": {
      rollNo: 4,
      marks: {
        "English": 49,
        "Urdu": 46,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 4,
        "Al-Quran": 9,
        "Oral Assessment": 10
      }
    },
    "Mushaf Haider": {
      rollNo: 5,
      marks: {
        "English": 49,
        "Urdu": 50,
        "Mathematics": 46,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 8,
        "Al-Quran": 7,
        "Oral Assessment": 10
      }
    },
    "Muhammad Meekal Haider": {
      rollNo: 6,
      marks: {
        "English": 50,
        "Urdu": 44,
        "Mathematics": 40,
        "General Science": 37,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 7,
        "Al-Quran": 8,
        "Oral Assessment": 10
      }
    },
    "Muhammad Eisa": {
      rollNo: 7,
      marks: {
        "English": 50,
        "Urdu": 49,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 8,
        "Al-Quran": 9,
        "Oral Assessment": 10
      }
    },
    "Muhammad Mujtaba": {
      rollNo: 8,
      marks: {
        "English": 50,
        "Urdu": 48,
        "Mathematics": 48,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 6,
        "Al-Quran": 9,
        "Oral Assessment": 10
      }
    },
    "Muhammad Asad Ali": {
      rollNo: 9,
      marks: {
        "English": 45,
        "Urdu": 49,
        "Mathematics": 50,
        "General Science": 45,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 9,
        "Al-Quran": 8,
        "Oral Assessment": 9
      }
    },
    "Muhammad Ahsan Shahmeer": {
      rollNo: 10,
      marks: {
        "English": 50,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 9,
        "Al-Quran": 9,
        "Oral Assessment": 10
      }
    },
    "Muhammad Araiz": {
      rollNo: 11,
      status: "SLC",
      isSLC: true,
      marks: {}
    },
    "Safeer Ali": {
      rollNo: 12,
      marks: {
        "English": 41,
        "Urdu": 34,
        "Mathematics": 50,
        "General Science": 49,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 18,
        "Drawing": 5,
        "Al-Quran": 8,
        "Oral Assessment": 10
      }
    },
    "Saifullah Akmal": {
      rollNo: 13,
      marks: {
        "English": 44,
        "Urdu": 23,
        "Mathematics": 40,
        "General Science": 50,
        "Computer": 9,
        "Social Studies": 28,
        "Islamiat": 19,
        "Drawing": 8,
        "Al-Quran": 7,
        "Oral Assessment": 7
      }
    },
    "Abdul Manan": {
      rollNo: 14,
      marks: {
        "English": 45,
        "Urdu": 22,
        "Mathematics": 22,
        "General Science": 44,
        "Computer": 9,
        "Social Studies": 24,
        "Islamiat": 9,
        "Drawing": 6,
        "Al-Quran": 3,
        "Oral Assessment": 3
      }
    },
    "Muhammad Hamza": {
      rollNo: 15,
      marks: {
        "English": 43,
        "Urdu": 25,
        "Mathematics": 45,
        "General Science": 46,
        "Computer": 8,
        "Social Studies": 29,
        "Islamiat": 7,
        "Drawing": 9,
        "Al-Quran": 6,
        "Oral Assessment": 8
      }
    },
    "Sultan Waheed": {
      rollNo: 16,
      marks: {
        "English": 45,
        "Urdu": 46,
        "Mathematics": 50,
        "General Science": 49,
        "Computer": 6,
        "Social Studies": 27,
        "Islamiat": 19,
        "Drawing": 8,
        "Al-Quran": 7,
        "Oral Assessment": 9
      }
    },
    "Muhammad Ismail": {
      rollNo: 17,
      marks: {
        "English": 48,
        "Urdu": 38,
        "Mathematics": 50,
        "General Science": 49,
        "Computer": 9,
        "Social Studies": 30,
        "Islamiat": 10,
        "Drawing": 7,
        "Al-Quran": 8,
        "Oral Assessment": 9
      }
    },
    "Awais Zaman": {
      rollNo: 18,
      marks: {
        "English": 39,
        "Urdu": 33,
        "Mathematics": 50,
        "General Science": 35,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 19,
        "Drawing": 4,
        "Al-Quran": 8,
        "Oral Assessment": 6
      }
    },
    "Muhammad Manan Ali": {
      rollNo: 19,
      marks: {
        "English": 50,
        "Urdu": 49,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 10,
        "Al-Quran": 2,
        "Oral Assessment": 8
      }
    },
    "Ghafoor Haider": {
      rollNo: 20,
      marks: {
        "English": 46,
        "Urdu": 26,
        "Mathematics": 44,
        "General Science": 37,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 9,
        "Drawing": 7,
        "Al-Quran": 8,
        "Oral Assessment": 10
      }
    },
    "Arslan Siddique": {
      rollNo: 21,
      marks: {
        "English": 49,
        "Urdu": 45,
        "Mathematics": 38,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 10,
        "Drawing": 9,
        "Al-Quran": 9,
        "Oral Assessment": 10
      }
    },
    "Muhammad Haseeb Ejaz": {
      rollNo: 22,
      marks: {
        "English": 48,
        "Urdu": 39,
        "Mathematics": 49,
        "General Science": 45,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 8,
        "Al-Quran": 7,
        "Oral Assessment": 10
      }
    },
    "Muhammad Uzair": {
      rollNo: 23,
      marks: {
        "English": 41,
        "Urdu": 44,
        "Mathematics": 49,
        "General Science": 49,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 8,
        "Al-Quran": 6,
        "Oral Assessment": 7
      }
    },
    "Haseeb Tariq": {
      rollNo: 24,
      marks: {
        "English": 33,
        "Urdu": 30,
        "Mathematics": 8,
        "General Science": 41,
        "Computer": 7,
        "Social Studies": 30,
        "Islamiat": 18,
        "Drawing": 0,
        "Al-Quran": 5,
        "Oral Assessment": 9
      }
    },
    "Muhammad Waleed": {
      rollNo: 25,
      marks: {
        "English": 48,
        "Urdu": 33,
        "Mathematics": 36,
        "General Science": 49,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 18,
        "Drawing": 5,
        "Al-Quran": 5,
        "Oral Assessment": 9
      }
    },
    "Muhammad Rehan": {
      rollNo: 26,
      marks: {
        "English": 46,
        "Urdu": 35,
        "Mathematics": 36,
        "General Science": 39,
        "Computer": 10,
        "Social Studies": 28,
        "Islamiat": 9,
        "Drawing": 8,
        "Al-Quran": 6,
        "Oral Assessment": 3
      }
    },
    "Arslan Tariq": {
      rollNo: 27,
      marks: {
        "English": 38,
        "Urdu": 34,
        "Mathematics": 28,
        "General Science": 48,
        "Computer": 9,
        "Social Studies": 30,
        "Islamiat": 18,
        "Drawing": 9,
        "Al-Quran": 7,
        "Oral Assessment": 7
      }
    },
    "Faizan Shoaib": {
      rollNo: 28,
      marks: {
        "English": 41,
        "Urdu": 32,
        "Mathematics": 14,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 18,
        "Drawing": 5,
        "Al-Quran": 9,
        "Oral Assessment": 6
      }
    },
    "Ali Hassan": {
      rollNo: 29,
      marks: {
        "English": 46,
        "Urdu": 40,
        "Mathematics": 40,
        "General Science": 48,
        "Computer": 10,
        "Social Studies": 29,
        "Islamiat": 19,
        "Drawing": 5,
        "Al-Quran": 7,
        "Oral Assessment": 8
      }
    },
    "Muhammad Shair": {
      rollNo: 30,
      marks: {
        "English": 40,
        "Urdu": 33,
        "Mathematics": 40,
        "General Science": 49,
        "Computer": 8,
        "Social Studies": 30,
        "Islamiat": 19,
        "Drawing": 6,
        "Al-Quran": 5,
        "Oral Assessment": 10
      }
    },
    "Saifullah Mubashir": {
      rollNo: 31,
      marks: {
        "English": 35,
        "Urdu": 17,
        "Mathematics": 0,
        "General Science": 41,
        "Computer": 10,
        "Social Studies": 20,
        "Islamiat": 15,
        "Drawing": 4,
        "Al-Quran": 4,
        "Oral Assessment": 6
      }
    },
    "Muhammad Usman Haider": {
      rollNo: 32,
      marks: {
        "English": 45,
        "Urdu": 49,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 8,
        "Al-Quran": 9,
        "Oral Assessment": 10
      }
    },
    "Farhan Sajid": {
      rollNo: 33,
      marks: {
        "English": 45,
        "Urdu": 48,
        "Mathematics": 50,
        "General Science": 39,
        "Computer": 10,
        "Social Studies": 27,
        "Islamiat": 19,
        "Drawing": 9,
        "Al-Quran": 7,
        "Oral Assessment": 9
      }
    }
  }
};

// Aliases for compatibility
const CLASS_5TH_BOYS_DATA = CLASS_DATA;

if (typeof window !== 'undefined') {
  window.CLASS_DATA = CLASS_DATA;
  window.CLASS_5TH_BOYS_DATA = CLASS_DATA;
}

if (typeof module !== 'undefined') {
  module.exports = { CLASS_DATA, CLASS_5TH_BOYS_DATA };
}
