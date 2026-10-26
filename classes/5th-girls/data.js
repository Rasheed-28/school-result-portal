/**
 * Academic Dataset: 5th Girls
 * Examination: 2nd Term 2026-27
 * Incharge: Sadaf Naureen
 * Principal: Dr. Shaukat Aziz
 * 
 * Source: Official 2nd Term Mark Sheet (Sadwal Campus)
 * Master copy of 5th Girls dataset.
 */

const CLASS_DATA = {
  meta: {
    id: "5th_girls",
    className: "5th",
    section: "Girls",
    fullName: "5th Girls",
    session: "2026-27",
    term: "2nd Term Examination",
    incharge: "Sadaf Naureen",
    principal: "Dr. Shaukat Aziz",
    date: "October 2026",
    passRate: 0.40 // 40% passing standard for Girls Section
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
    "Mahnoor Zahra": {
      rollNo: 1,
      marks: {
        "English": 50,
        "Urdu": 49,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 10,
        "Al-Quran": 10,
        "Oral Assessment": 10
      }
    },
    "Rida Mubeen": {
      rollNo: 2,
      marks: {
        "English": 50,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 10,
        "Drawing": 10,
        "Al-Quran": 10,
        "Oral Assessment": 9
      }
    },
    "Rania Noor": {
      rollNo: 3,
      marks: {
        "English": 50,
        "Urdu": 48,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 7,
        "Al-Quran": 10,
        "Oral Assessment": 9
      }
    },
    "Eshaal Anum": {
      rollNo: 4,
      marks: {
        "English": 50,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 9,
        "Al-Quran": 10,
        "Oral Assessment": 10
      }
    },
    "Imsaal Zahra": {
      rollNo: 5,
      marks: {
        "English": 49,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 9,
        "Al-Quran": 9,
        "Oral Assessment": 9
      }
    },
    "Anaya Javed": {
      rollNo: 6,
      marks: {
        "English": 50,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 9,
        "Al-Quran": 10,
        "Oral Assessment": 10
      }
    },
    "Laraib Jameel": {
      rollNo: 7,
      marks: {
        "English": 48,
        "Urdu": 48,
        "Mathematics": 17,
        "General Science": 49,
        "Computer": 8,
        "Social Studies": 30,
        "Islamiat": 18,
        "Drawing": 7,
        "Al-Quran": 9,
        "Oral Assessment": 6
      }
    },
    "Ajwa Noor": {
      rollNo: 8,
      marks: {
        "English": 49,
        "Urdu": 44,
        "Mathematics": 47,
        "General Science": 49,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 10,
        "Al-Quran": 9,
        "Oral Assessment": 10
      }
    },
    "Tooba Shehbaz": {
      rollNo: 9,
      marks: {
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
      }
    },
    "Zobabsh Fakhar": {
      rollNo: 10,
      marks: {
        "English": 48,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 19,
        "Drawing": 8,
        "Al-Quran": 10,
        "Oral Assessment": 10
      }
    },
    "Hajra Noor": {
      rollNo: 11,
      marks: {
        "English": 49,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 9,
        "Al-Quran": 10,
        "Oral Assessment": 10
      }
    },
    "Aleesha Nasir": {
      rollNo: 12,
      marks: {
        "English": 50,
        "Urdu": 50,
        "Mathematics": 50,
        "General Science": 49,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 10,
        "Drawing": 9,
        "Al-Quran": 10,
        "Oral Assessment": 10
      }
    },
    "Fatima Zahra": {
      rollNo: 13,
      marks: {
        "English": 43,
        "Urdu": 41,
        "Mathematics": 50,
        "General Science": 49,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 10,
        "Al-Quran": 8,
        "Oral Assessment": 8
      }
    },
    "Eshaal Fatima": {
      rollNo: 14,
      marks: {
        "English": 41,
        "Urdu": 30,
        "Mathematics": 18,
        "General Science": 23,
        "Computer": 9,
        "Social Studies": 23,
        "Islamiat": 9,
        "Drawing": 8,
        "Al-Quran": 8,
        "Oral Assessment": 2
      }
    },
    "Areesha Fatima": {
      rollNo: 15,
      marks: {
        "English": 49,
        "Urdu": 46,
        "Mathematics": 50,
        "General Science": 50,
        "Computer": 10,
        "Social Studies": 30,
        "Islamiat": 20,
        "Drawing": 9,
        "Al-Quran": 10,
        "Oral Assessment": 10
      }
    }
  }
};

// Aliases for compatibility
const CLASS_5TH_GIRLS_DATA = CLASS_DATA;

if (typeof window !== 'undefined') {
  window.CLASS_DATA = CLASS_DATA;
  window.CLASS_5TH_GIRLS_DATA = CLASS_DATA;
}

if (typeof module !== 'undefined') {
  module.exports = { CLASS_DATA, CLASS_5TH_GIRLS_DATA };
}
