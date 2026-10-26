/**
 * Academic Dataset: 6th Girls
 * Examination: 2nd Term 2026-27
 * Incharge: Tayyaba Hina
 * Principal: Dr. Shaukat Aziz
 * 
 * Source: Official 2nd Term Mark Sheet (Sadwal Campus)
 * Master copy of 6th Girls dataset.
 */

const CLASS_DATA = {
  meta: {
    id: "6th_girls",
    className: "6th",
    section: "Girls",
    fullName: "6th Girls",
    session: "2026-27",
    term: "2nd Term Examination",
    incharge: "Tayyaba Hina",
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
    "History & Geo": 50
  },
  // Student Name as Object Key with Subject Marks as Key-Value Pairs
  students: {
    "Marosh Muatter": {
      rollNo: 1,
      marks: {
        "English": 37,
        "Urdu": 47,
        "Mathematics": 48,
        "General Science": 48,
        "Computer Science": 41,
        "Al-Quran": 40,
        "Islamiat": 49,
        "Drawing": 9,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "History & Geo": 50
      }
    },
    "Minahil Fatima": {
      rollNo: 2,
      marks: {
        "English": 48,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 47,
        "Computer Science": 48,
        "Al-Quran": 50,
        "Islamiat": 50,
        "Drawing": 10,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "History & Geo": 50
      }
    },
    "Nawal Fatima": {
      rollNo: 3,
      marks: {
        "English": 33,
        "Urdu": 43,
        "Mathematics": 32,
        "General Science": 30,
        "Computer Science": 39,
        "Al-Quran": 50,
        "Islamiat": 49,
        "Drawing": 6,
        "Model Making": 4,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 9,
        "History & Geo": 49
      }
    },
    "Khadjia Mansoor": {
      rollNo: 4,
      marks: {
        "English": 37,
        "Urdu": 49,
        "Mathematics": 50,
        "General Science": 43,
        "Computer Science": 46,
        "Al-Quran": 50,
        "Islamiat": 49,
        "Drawing": 9,
        "Model Making": 4,
        "Al-Quran (Oral)": 4,
        "Oral Assessment": 8,
        "History & Geo": 50
      }
    },
    "Maryam Noor": {
      rollNo: 5,
      marks: {
        "English": 39,
        "Urdu": 48,
        "Mathematics": 32,
        "General Science": 13,
        "Computer Science": 31,
        "Al-Quran": 49,
        "Islamiat": 50,
        "Drawing": 8,
        "Model Making": 4,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 9,
        "History & Geo": 47
      }
    },
    "Dua Fatima": {
      rollNo: 6,
      marks: {
        "English": 40,
        "Urdu": 46,
        "Mathematics": 39,
        "General Science": 45,
        "Computer Science": 37,
        "Al-Quran": 49,
        "Islamiat": 50,
        "Drawing": 9,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "History & Geo": 49
      }
    },
    "Mishaim Zahra": {
      rollNo: 7,
      marks: {
        "English": 43,
        "Urdu": 49,
        "Mathematics": 48,
        "General Science": 30,
        "Computer Science": 47,
        "Al-Quran": 50,
        "Islamiat": 50,
        "Drawing": 10,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 8,
        "History & Geo": 49
      }
    },
    "Um-e-Fatima": {
      rollNo: 8,
      marks: {
        "English": 39,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 50,
        "Computer Science": 48,
        "Al-Quran": 50,
        "Islamiat": 50,
        "Drawing": 10,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "History & Geo": 50
      }
    },
    "Maira Jabeen": {
      rollNo: 9,
      marks: {
        "English": 9,
        "Urdu": 13,
        "Mathematics": 40,
        "General Science": 0,
        "Computer Science": 3,
        "Al-Quran": 20,
        "Islamiat": 21,
        "Drawing": 7,
        "Model Making": 4,
        "Al-Quran (Oral)": 5,
        "Oral Assessment": 8,
        "History & Geo": 24
      }
    },
    "Eshaal Fatima": {
      rollNo: 10,
      marks: {
        "English": 45,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 47,
        "Computer Science": 45,
        "Al-Quran": 50,
        "Islamiat": 50,
        "Drawing": 10,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "History & Geo": 50
      }
    },
    "Sidra Soaib": {
      rollNo: 11,
      marks: {
        "English": "-",
        "Urdu": "-",
        "Mathematics": "-",
        "General Science": "-",
        "Computer Science": "-",
        "Al-Quran": "-",
        "Islamiat": "-",
        "Drawing": "-",
        "Model Making": "-",
        "Al-Quran (Oral)": "-",
        "Oral Assessment": "-",
        "History & Geo": "-"
      }
    },
    "Abrish Hourain": {
      rollNo: 12,
      marks: {
        "English": 44,
        "Urdu": 48,
        "Mathematics": 35,
        "General Science": 47,
        "Computer Science": 42,
        "Al-Quran": 49,
        "Islamiat": 50,
        "Drawing": 7,
        "Model Making": 4,
        "Al-Quran (Oral)": 9,
        "Oral Assessment": 10,
        "History & Geo": 49
      }
    },
    "Tehreem Zahra": {
      rollNo: 13,
      marks: {
        "English": 28,
        "Urdu": 36,
        "Mathematics": 30,
        "General Science": 8,
        "Computer Science": 36,
        "Al-Quran": 49,
        "Islamiat": 49,
        "Drawing": 4,
        "Model Making": 3,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "History & Geo": 39
      }
    },
    "Aleesha Murtaza": {
      rollNo: 14,
      marks: {
        "English": 31,
        "Urdu": 29,
        "Mathematics": 34,
        "General Science": 7,
        "Computer Science": 21,
        "Al-Quran": 46,
        "Islamiat": 42,
        "Drawing": 7,
        "Model Making": 4,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "History & Geo": 30
      }
    },
    "Ayesha Siddiqa": {
      rollNo: 15,
      marks: {
        "English": 27,
        "Urdu": 35,
        "Mathematics": 27,
        "General Science": 10,
        "Computer Science": 13,
        "Al-Quran": 40,
        "Islamiat": 18,
        "Drawing": 8,
        "Model Making": 4,
        "Al-Quran (Oral)": 9,
        "Oral Assessment": 10,
        "History & Geo": 37
      }
    },
    "Hadia Imran": {
      rollNo: 16,
      marks: {
        "English": 37,
        "Urdu": 50,
        "Mathematics": 49,
        "General Science": 47,
        "Computer Science": 45,
        "Al-Quran": 49,
        "Islamiat": 48,
        "Drawing": 9,
        "Model Making": 5,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 9,
        "History & Geo": 50
      }
    },
    "Abrish Noor": {
      rollNo: 17,
      marks: {
        "English": 37,
        "Urdu": 32,
        "Mathematics": 26,
        "General Science": 19,
        "Computer Science": 43,
        "Al-Quran": 41,
        "Islamiat": 49,
        "Drawing": 7,
        "Model Making": 4,
        "Al-Quran (Oral)": 10,
        "Oral Assessment": 10,
        "History & Geo": 38
      }
    }
  }
};

// Aliases for compatibility
const CLASS_6TH_GIRLS_DATA = CLASS_DATA;

if (typeof window !== 'undefined') {
  window.CLASS_DATA = CLASS_DATA;
  window.CLASS_6TH_GIRLS_DATA = CLASS_DATA;
}

if (typeof module !== 'undefined') {
  module.exports = { CLASS_DATA, CLASS_6TH_GIRLS_DATA };
}
