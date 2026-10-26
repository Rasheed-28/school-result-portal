/**
 * Academic Dataset: 7th Boys
 * Examination: 2nd Term 2026-27
 * Incharge: Laiba Batool
 * Principal: Dr. Shaukat Aziz
 * 
 * Source: Official 2nd Term Mark Sheet (Sadwal Campus)
 * Master copy of 7th Boys dataset.
 */

const CLASS_DATA = {
  meta: {
    id: "7th_boys",
    className: "7th",
    section: "Boys",
    fullName: "7th Boys",
    session: "2026-27",
    term: "2nd Term Examination",
    incharge: "Laiba Batool",
    principal: "Dr. Shaukat Aziz",
    date: "October 2026",
    passRate: 0.40 // 40% passing standard for Boys Section
  },
  // Subjects and their maximum marks (Total: 435)
  subjects: {
    "English": 50,
    "Urdu": 50,
    "Mathematics": 50,
    "General Science": 50,
    "Computer Science": 50,
    "Al-Quran": 50,
    "Islamiat": 50,
    "Drawing": 10,
    "Model Making": 5,
    "Al-Quran (Oral)": 10,
    "Oral Assessment": 10,
    "History & Geo": 50
  },
  // Student Name as Object Key with Subject Marks as Key-Value Pairs
  students: {
    "Abdul Raheem": {
      rollNo: 1,
      marks: {
        "English": 49,
        "Urdu": 39,
        "Mathematics": 49,
        "General Science": 42,
        "Computer Science": 49,
        "Al-Quran": 46,
        "Islamiat": 48,
        "Drawing": 7,
        "Model Making": 4,
        "Al-Quran (Oral)": 8,
        "Oral Assessment": 9,
        "History & Geo": 40
      }
    },
    "Muhammad Issam": {
      rollNo: 2,
      marks: {
        "English": 41,
        "Urdu": 32,
        "Mathematics": 48,
        "General Science": 35,
        "Computer Science": 47,
        "Al-Quran": 44,
        "Islamiat": 47,
        "Drawing": 8,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "History & Geo": 43
      }
    },
    "Abdul Hadi": {
      rollNo: 3,
      marks: {
        "English": 50,
        "Urdu": 47,
        "Mathematics": 50,
        "General Science": 50,
        "Computer Science": 50,
        "Al-Quran": 48,
        "Islamiat": 50,
        "Drawing": 9,
        "Model Making": 4,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 8,
        "History & Geo": 50
      }
    },
    "Hashim Ali": {
      rollNo: 4,
      marks: {
        "English": 43,
        "Urdu": 39,
        "Mathematics": 48,
        "General Science": 38,
        "Computer Science": 36,
        "Al-Quran": 40,
        "Islamiat": 32,
        "Drawing": 7,
        "Model Making": 3,
        "Al-Quran (Oral)": 6,
        "Oral Assessment": 8,
        "History & Geo": 36
      }
    },
    "Zubair Ali": {
      rollNo: 5,
      marks: {
        "English": 48,
        "Urdu": 39,
        "Mathematics": 50,
        "General Science": 35,
        "Computer Science": 48,
        "Al-Quran": 49,
        "Islamiat": 48,
        "Drawing": 8,
        "Model Making": 3,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "History & Geo": 40
      }
    },
    "Muhammad Afan": {
      rollNo: 6,
      marks: {
        "English": 45,
        "Urdu": 38,
        "Mathematics": 50,
        "General Science": 39,
        "Computer Science": 44,
        "Al-Quran": 39,
        "Islamiat": 46,
        "Drawing": 1,
        "Model Making": 3,
        "Al-Quran (Oral)": 9,
        "Oral Assessment": 10,
        "History & Geo": 43
      }
    },
    "Dayan Umar": {
      rollNo: 7,
      marks: {
        "English": 49,
        "Urdu": 42,
        "Mathematics": 40,
        "General Science": 49,
        "Computer Science": 49,
        "Al-Quran": 48,
        "Islamiat": 50,
        "Drawing": 8,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 9,
        "History & Geo": 50
      }
    },
    "Abdul Rehman": {
      rollNo: 8,
      marks: {
        "English": 39,
        "Urdu": 29,
        "Mathematics": 50,
        "General Science": 46,
        "Computer Science": 47,
        "Al-Quran": 43,
        "Islamiat": 49,
        "Drawing": 7,
        "Model Making": 3,
        "Al-Quran (Oral)": 9,
        "Oral Assessment": 10,
        "History & Geo": 39
      }
    },
    "Muhammad Alyan": {
      rollNo: 9,
      marks: {
        "English": 41,
        "Urdu": 40,
        "Mathematics": 48,
        "General Science": 37,
        "Computer Science": 47,
        "Al-Quran": 37,
        "Islamiat": 48,
        "Drawing": 8,
        "Model Making": 3,
        "Al-Quran (Oral)": 8,
        "Oral Assessment": 9,
        "History & Geo": 49
      }
    },
    "Muhammad Sharjeel": {
      rollNo: 10,
      marks: {
        "English": 45,
        "Urdu": 38,
        "Mathematics": 48,
        "General Science": 43,
        "Computer Science": 46,
        "Al-Quran": 46,
        "Islamiat": 46,
        "Drawing": 7,
        "Model Making": 3,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 9,
        "History & Geo": 48
      }
    },
    "Umer Farooq": {
      rollNo: 11,
      marks: {
        "English": 43,
        "Urdu": 25,
        "Mathematics": 37,
        "General Science": 44,
        "Computer Science": 39,
        "Al-Quran": 42,
        "Islamiat": 50,
        "Drawing": 10,
        "Model Making": 4,
        "Al-Quran (Oral)": 8,
        "Oral Assessment": 9,
        "History & Geo": 38
      }
    },
    "Muaz Ali": {
      rollNo: 12,
      marks: {
        "English": 42,
        "Urdu": 33,
        "Mathematics": 50,
        "General Science": 36,
        "Computer Science": 47,
        "Al-Quran": 41,
        "Islamiat": 47,
        "Drawing": 3,
        "Model Making": 3,
        "Al-Quran (Oral)": 9,
        "Oral Assessment": 9,
        "History & Geo": 41
      }
    },
    "Zain Ali": {
      rollNo: 13,
      marks: {
        "English": 48,
        "Urdu": 26,
        "Mathematics": 40,
        "General Science": 37,
        "Computer Science": 49,
        "Al-Quran": 47,
        "Islamiat": 43,
        "Drawing": 7,
        "Model Making": 4,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 8,
        "History & Geo": 40
      }
    },
    "Ali Haider": {
      rollNo: 14,
      marks: {
        "English": 39,
        "Urdu": 18,
        "Mathematics": 39,
        "General Science": 22,
        "Computer Science": 48,
        "Al-Quran": 43,
        "Islamiat": 16,
        "Drawing": 5,
        "Model Making": 3,
        "Al-Quran (Oral)": 3,
        "Oral Assessment": 8,
        "History & Geo": 15
      }
    },
    "Ikhlas Haider": {
      rollNo: 15,
      marks: {
        "English": 48,
        "Urdu": 42,
        "Mathematics": 50,
        "General Science": 47,
        "Computer Science": 48,
        "Al-Quran": 44,
        "Islamiat": 49,
        "Drawing": 7,
        "Model Making": 3,
        "Al-Quran (Oral)": 8,
        "Oral Assessment": 9,
        "History & Geo": 50
      }
    },
    "Muhammad Aleem Ahmed": {
      rollNo: 16,
      marks: {
        "English": 38,
        "Urdu": 40,
        "Mathematics": 49,
        "General Science": 48,
        "Computer Science": 47,
        "Al-Quran": 47,
        "Islamiat": 49,
        "Drawing": 4,
        "Model Making": 2,
        "Al-Quran (Oral)": 9,
        "Oral Assessment": 10,
        "History & Geo": 49
      }
    }
  }
};

// Aliases for compatibility
const CLASS_7TH_BOYS_DATA = CLASS_DATA;

if (typeof window !== 'undefined') {
  window.CLASS_DATA = CLASS_DATA;
  window.CLASS_7TH_BOYS_DATA = CLASS_DATA;
}

if (typeof module !== 'undefined') {
  module.exports = { CLASS_DATA, CLASS_7TH_BOYS_DATA };
}