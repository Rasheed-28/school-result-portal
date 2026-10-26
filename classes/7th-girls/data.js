/**
 * Academic Dataset: 7th Girls
 * Examination: 2nd Term 2026-27
 * Incharge: Amna Feroz
 * Principal: Dr. Shaukat Aziz
 * 
 * Source: Official 2nd Term Mark Sheet (Sadwal Campus)
 * Master copy of 7th Girls dataset.
 */

const CLASS_DATA = {
  meta: {
    id: "7th_girls",
    className: "7th",
    section: "Girls",
    fullName: "7th Girls",
    session: "2026-27",
    term: "2nd Term Examination",
    incharge: "Amna Feroz",
    principal: "Dr. Shaukat Aziz",
    date: "October 2026",
    passRate: 0.40 // 40% passing standard for Girls Section
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
    "Geography": 50
  },
  // Student Name as Object Key with Subject Marks as Key-Value Pairs
  students: {
    "Misbah Nawaz": {
      rollNo: 1,
      marks: {
        "English": 49,
        "Urdu": 44,
        "Mathematics": 50,
        "General Science": 50,
        "Computer Science": 50,
        "Al-Quran": 49,
        "Islamiat": 48,
        "Drawing": 10,
        "Model Making": 2,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "Geography": 50
      }
    },
    "Anabia Tehneat": {
      rollNo: 2,
      marks: {
        "English": 43,
        "Urdu": 48,
        "Mathematics": 50,
        "General Science": 49,
        "Computer Science": 42,
        "Al-Quran": 44,
        "Islamiat": 48,
        "Drawing": 10,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "Geography": 50
      }
    },
    "Urwa Eiman": {
      rollNo: 3,
      marks: {
        "English": 40,
        "Urdu": 32,
        "Mathematics": 30,
        "General Science": 50,
        "Computer Science": 50,
        "Al-Quran": 45,
        "Islamiat": 38,
        "Drawing": 7,
        "Model Making": 4,
        "Al-Quran (Oral)": 9,
        "Oral Assessment": 8,
        "Geography": 46
      }
    },
    "Rameen Kanwal": {
      rollNo: 4,
      marks: {
        "English": 50,
        "Urdu": 49,
        "Mathematics": 50,
        "General Science": 50,
        "Computer Science": 50,
        "Al-Quran": 50,
        "Islamiat": 50,
        "Drawing": 10,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "Geography": 50
      }
    },
    "Zarlish Nadia": {
      rollNo: 5,
      marks: {
        "English": 50,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 50,
        "Computer Science": 50,
        "Al-Quran": 49,
        "Islamiat": 50,
        "Drawing": 10,
        "Model Making": 4,
        "Al-Quran (Oral)": 8,
        "Oral Assessment": 10,
        "Geography": 50
      }
    },
    "Fatima Noor-ul-Ain": {
      rollNo: 6,
      marks: {
        "English": 50,
        "Urdu": 49,
        "Mathematics": 50,
        "General Science": 50,
        "Computer Science": 50,
        "Al-Quran": 50,
        "Islamiat": 50,
        "Drawing": 10,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "Geography": 50
      }
    },
    "Areeba Humayun": {
      rollNo: 7,
      marks: {
        "English": 50,
        "Urdu": 46,
        "Mathematics": 50,
        "General Science": 50,
        "Computer Science": 49,
        "Al-Quran": 46,
        "Islamiat": 48,
        "Drawing": 8,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "Geography": 48
      }
    },
    "Rameen Fatima": {
      rollNo: 8,
      marks: {
        "English": 50,
        "Urdu": 49,
        "Mathematics": 50,
        "General Science": 49,
        "Computer Science": 48,
        "Al-Quran": 44,
        "Islamiat": 45,
        "Drawing": 7.5,
        "Model Making": 4,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "Geography": 50
      }
    },
    "Rabia Eiman": {
      rollNo: 9,
      marks: {
        "English": 50,
        "Urdu": 47,
        "Mathematics": 50,
        "General Science": 49,
        "Computer Science": 49,
        "Al-Quran": 45,
        "Islamiat": 31,
        "Drawing": 10,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "Geography": 50
      }
    },
    "Malaika Insar": {
      rollNo: 10,
      marks: {
        "English": 45,
        "Urdu": 44,
        "Mathematics": 40,
        "General Science": 40,
        "Computer Science": 50,
        "Al-Quran": 49,
        "Islamiat": 40,
        "Drawing": 9,
        "Model Making": 5,
        "Al-Quran (Oral)": 9,
        "Oral Assessment": 8,
        "Geography": 50
      }
    },
    "Eshal Fatima": {
      rollNo: 11,
      marks: {
        "English": 50,
        "Urdu": 49,
        "Mathematics": 50,
        "General Science": 50,
        "Computer Science": 50,
        "Al-Quran": 50,
        "Islamiat": 49,
        "Drawing": 10,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "Geography": 50
      }
    },
    "Abrish Noor": {
      rollNo: 12,
      marks: {
        "English": 49,
        "Urdu": 48,
        "Mathematics": 50,
        "General Science": 49,
        "Computer Science": 49,
        "Al-Quran": 48,
        "Islamiat": 50,
        "Drawing": 7,
        "Model Making": 4,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "Geography": 49
      }
    }
  }
};

// Aliases for compatibility
const CLASS_7TH_GIRLS_DATA = CLASS_DATA;

if (typeof window !== 'undefined') {
  window.CLASS_DATA = CLASS_DATA;
  window.CLASS_7TH_GIRLS_DATA = CLASS_DATA;
}

if (typeof module !== 'undefined') {
  module.exports = { CLASS_DATA, CLASS_7TH_GIRLS_DATA };
}
