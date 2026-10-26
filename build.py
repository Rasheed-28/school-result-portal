#!/usr/bin/env python3
"""
Academic Result Management System - Al Rehman Public Secondary School
Build Script: Generates all print-ready HTML files with calibrated 1-page-per-sheet landscape PDF layout.
"""
import os, subprocess, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Read Assets
with open(os.path.join(BASE_DIR, 'assets', 'logo_base64.js'), 'r', encoding='utf-8') as f:
    logo_file_content = f.read()
    start_q = logo_file_content.find('"')
    if start_q == -1: start_q = logo_file_content.find("'")
    end_q = logo_file_content.rfind('"')
    if end_q <= start_q: end_q = logo_file_content.rfind("'")
    logo_base64 = logo_file_content[start_q+1:end_q].strip()

with open(os.path.join(BASE_DIR, 'shared', 'engine.js'), 'r', encoding='utf-8') as f:
    engine_js = f.read().strip()

with open(os.path.join(BASE_DIR, 'data', 'class_7th_boys.js'), 'r', encoding='utf-8') as f:
    class_7th_boys_js = f.read().strip()

EMBEDDED_SCRIPTS = """
  <!-- Shared Core Engine & Class Common Data File -->
  <script src="../../assets/logo_base64.js"></script>
  <script src="../../shared/engine.js"></script>
  <script src="data.js"></script>
"""

# =========================================================================
# 1. CARDS TEMPLATE (2 per landscape page, GUARANTEED exactly 1 page per sheet)
# =========================================================================
cards_tpl = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>7th Boys - Student Result Cards (Landscape 2-Per-Page)</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: 'Inter', sans-serif;
      -webkit-font-smoothing: antialiased;
      background-color: #f1f5f9;
      margin: 0;
      padding: 0;
    }
    .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }
    .logo-sharp {
      image-rendering: -webkit-optimize-contrast;
      image-rendering: crisp-edges;
    }
    
    /* Exact A4 Landscape PDF Print Geometry */
    @page {
      size: 297mm 210mm;
      margin: 0;
    }
    
    @media print {
      html, body {
        width: 297mm !important;
        height: 210mm !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #ffffff !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      .no-print {
        display: none !important;
      }
      #cards-container {
        padding: 0 !important;
        margin: 0 auto !important;
        max-width: none !important;
        width: 297mm !important;
        gap: 0 !important;
        space-y: 0 !important;
      }
      .landscape-sheet {
        width: 297mm !important;
        height: 210mm !important;
        max-height: 210mm !important;
        page-break-after: always !important;
        break-after: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin: 0 !important;
        padding: 4.5mm 8mm !important;
        box-sizing: border-box !important;
        border: none !important;
        box-shadow: none !important;
        overflow: hidden !important;
        display: block !important;
      }
      .landscape-sheet:last-child {
        page-break-after: avoid !important;
        break-after: avoid !important;
      }
    }

    @media screen {
      #cards-container {
        width: 100%;
        max-width: 1240px;
        margin: 0 auto;
        padding: 24px 0;
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      .landscape-sheet {
        width: 297mm;
        height: 210mm;
        max-height: 210mm;
        padding: 4.5mm 8mm;
        box-sizing: border-box;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 24px;
        background: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      }
    }

    /* Balanced 2-Card Layout Rules (Fail-safe with or without CDN) */
    .cards-row {
      width: 100% !important;
      height: 100% !important;
      display: flex !important;
      flex-direction: row !important;
      align-items: stretch !important;
      justify-content: space-between !important;
      gap: 16px !important;
      box-sizing: border-box !important;
    }
    .card-wrapper {
      flex: 1 1 0% !important;
      min-width: 0 !important;
      height: 100% !important;
      box-sizing: border-box !important;
    }
    .card-box {
      width: 100% !important;
      height: 100% !important;
      border: 1.5px solid #334155 !important;
      border-radius: 8px !important;
      padding: 10px !important;
      background: #ffffff !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-between !important;
      box-sizing: border-box !important;
      position: relative !important;
    }
    .cutter-gutter {
      width: 28px !important;
      flex-shrink: 0 !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      justify-content: space-between !important;
      padding: 8px 0 !important;
      color: #94a3b8 !important;
      user-select: none !important;
      box-sizing: border-box !important;
    }
    .cutter-line {
      flex: 1 !important;
      width: 0 !important;
      border-right: 2px dashed #cbd5e1 !important;
      margin: 4px 0 !important;
    }
    .navbar-container {
      width: 100%;
      background: rgba(255, 255, 255, 0.98);
      border-bottom: 1px solid #e2e8f0;
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    }
  </style>
</head>
<body class="bg-slate-100 text-slate-900">

  <!-- Print Navigation Bar -->
  <div class="no-print navbar-container">
    <div class="flex items-center space-x-3" style="display: flex; align-items: center; gap: 12px;">
      <img src="logo.jpg" onerror="this.src=SCHOOL_LOGO_BASE64; this.onerror=null;" alt="School Logo" class="h-10 w-10 object-contain logo-sharp border border-slate-300 rounded-full" style="width: 40px; height: 40px; object-fit: contain; border-radius: 9999px;">
      <div>
        <h1 class="text-sm font-bold text-slate-800" style="font-size: 14px; font-weight: 700; color: #1e293b; margin: 0;">Al Rehman Public Secondary School Sadwal (Chakwal)</h1>
        <p class="text-xs text-slate-500" style="font-size: 12px; color: #64748b; margin: 0;">Student Result Cards &bull; 7th Boys &bull; 2 Cards per Landscape Sheet (1 Page per Sheet)</p>
      </div>
    </div>
    <div class="flex items-center space-x-3" style="display: flex; align-items: center; gap: 12px;">
      <a href="../../index.html" class="inline-flex items-center px-3 py-1.5 text-xs font-medium text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-md border border-slate-300 transition" style="display: inline-flex; align-items: center; padding: 6px 12px; font-size: 12px; font-weight: 500; color: #334155; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none;">
        &larr; Master Hub
      </a>
      <a href="marksheet.html" class="inline-flex items-center px-3 py-1.5 text-xs font-medium text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-md border border-slate-300 transition" style="display: inline-flex; align-items: center; padding: 6px 12px; font-size: 12px; font-weight: 500; color: #334155; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none;">
        Consolidated Sheet
      </a>
      <a href="failure_sheet.html" class="inline-flex items-center px-3 py-1.5 text-xs font-medium text-rose-700 bg-rose-50 hover:bg-rose-100 rounded-md border border-rose-200 transition" style="display: inline-flex; align-items: center; padding: 6px 12px; font-size: 12px; font-weight: 500; color: #be123c; background: #fff1f2; border: 1px solid #fecdd3; border-radius: 6px; text-decoration: none;">
        Failure Sheet
      </a>
      <button onclick="window.print()" class="inline-flex items-center space-x-1.5 bg-slate-900 hover:bg-slate-800 text-white text-xs font-semibold px-4 py-2 rounded-md shadow transition" style="display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; font-size: 12px; font-weight: 600; color: #ffffff; background: #0f172a; border: none; border-radius: 6px; cursor: pointer;">
        <svg class="w-4 h-4" style="width: 16px; height: 16px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
        <span>Print Landscape PDF (Ctrl+P)</span>
      </button>
    </div>
  </div>

  <div id="cards-container" class="w-full max-w-[1240px] mx-auto p-4 space-y-6 flex flex-col items-center">
    <!-- Rendered by JS -->
  </div>

  __SCRIPTS__

  <script>
  function renderResultCard(st, classData) {
    const rowsHtml = st.subjectResults.map((sub, i) => {
      const isFailed = !sub.isPass;
      const rowBg = isFailed ? 'bg-rose-50/90 font-semibold' : (i % 2 === 0 ? 'bg-white' : 'bg-slate-50/70');
      const markDisplay = isFailed 
        ? `<span class="text-rose-700 font-bold font-mono text-xs">${sub.mark}*</span>` 
        : `<span class="font-bold text-slate-900 font-mono text-xs">${sub.mark}</span>`;
      const statusBadge = isFailed 
        ? `<span class="inline-block px-1.5 py-0.2 rounded text-[9px] font-bold bg-rose-100 text-rose-700 border border-rose-300">Fail</span>` 
        : `<span class="inline-block px-1.5 py-0.2 rounded text-[9px] font-bold text-emerald-700 bg-emerald-50">Pass</span>`;

      // Guarantee clean display subject title
      const displayTitle = (sub.title || '').replace(/\\(Nazra\\)/gi, '').replace(/Nazra/gi, 'Al-Quran').replace(/\\s+/g, ' ').trim();

      return `
        <tr class="${rowBg} border-b border-slate-200">
          <td class="py-0.5 px-2 text-center text-slate-400 font-mono text-[10px]">${i + 1}</td>
          <td class="py-0.5 px-2.5 text-slate-900 font-semibold text-xs">${displayTitle}</td>
          <td class="py-0.5 px-2 text-center text-slate-600 font-mono text-xs">${sub.maxMarks}</td>
          <td class="py-0.5 px-2 text-center">${markDisplay}</td>
          <td class="py-0.5 px-2 text-center">${statusBadge}</td>
        </tr>
      `;
    }).join('');

    return `
      <div class="card-box h-full border-[1.5px] border-slate-700 rounded-lg bg-white p-2.5 flex flex-col justify-between shadow-sm relative text-slate-900 box-border">
        
        <!-- Header -->
        <div class="border-b-[1.5px] border-slate-800 pb-1 mb-1">
          <div class="flex items-center space-x-2.5">
            <img src="logo.jpg" 
                 onerror="if (this.src.indexOf('assets') === -1) { this.src='../../assets/logo.jpg'; } else { this.src=SCHOOL_LOGO_BASE64; }"
                 alt="School Logo" 
                 class="h-14 w-14 object-contain logo-sharp flex-shrink-0">
            <div class="flex-1 text-center pr-1">
              <h2 class="text-[13px] font-black uppercase tracking-tight text-slate-900 leading-tight">
                Al Rehman Public Secondary School Sadwal
              </h2>
              <div class="flex items-center justify-center space-x-2 text-[9px] text-slate-600 font-semibold mt-0.5">
                <span>Sadwal (Chakwal)</span>
                <span>&bull;</span>
                <span class="italic text-slate-700 font-serif">"Enter to Learn - Leave to Serve"</span>
              </div>
              
              <!-- Badge with vertical padding -->
              <div class="inline-block my-1 bg-slate-900 text-white font-extrabold text-[9.5px] px-4 py-1 rounded-full uppercase tracking-wider shadow-sm">
                Student Progress Report &bull; 2nd Term 2026-27
              </div>
            </div>
          </div>

          <!-- Student Profile Strip -->
          <div class="grid grid-cols-3 gap-1 mt-1 pt-1 border-t border-slate-200 text-xs bg-slate-50/90 py-1 px-2 rounded text-center">
            <div>
              <span class="text-slate-500 block text-[8px] uppercase font-bold tracking-wider">Roll / Sr No</span>
              <span class="font-black text-slate-900 font-mono text-xs">#${String(st.sr).padStart(2, '0')}</span>
            </div>
            <div>
              <span class="text-slate-500 block text-[8px] uppercase font-bold tracking-wider">Student Name</span>
              <span class="font-black text-slate-900 text-xs truncate block">${st.name}</span>
            </div>
            <div>
              <span class="text-slate-500 block text-[8px] uppercase font-bold tracking-wider">Class & Section</span>
              <span class="font-black text-slate-800 text-xs">${classData.meta.fullName}</span>
            </div>
          </div>
        </div>

        <!-- Subject Marks Table (5 Clean Columns, Calibrated Height) -->
        <div class="flex-1 my-0.5">
          <table class="w-full text-left border-collapse border border-slate-300">
            <thead>
              <tr class="bg-slate-800 text-white text-[10px] uppercase font-extrabold tracking-wider">
                <th class="py-1 px-1.5 text-center w-7">#</th>
                <th class="py-1 px-2.5">Subject Name</th>
                <th class="py-1 px-2 text-center w-16">Total Marks</th>
                <th class="py-1 px-2 text-center w-20">Marks Obtained</th>
                <th class="py-1 px-2 text-center w-16">Status</th>
              </tr>
            </thead>
            <tbody>
              ${rowsHtml}
            </tbody>
            <tfoot>
              <tr class="bg-slate-100 font-bold text-xs border-t-2 border-slate-700">
                <td colspan="2" class="py-1 px-2.5 text-slate-900 font-black uppercase text-[11px]">Total Marks Summary</td>
                <td class="py-1 px-2 text-center font-mono text-slate-700 text-xs font-bold">435</td>
                <td class="py-1 px-2 text-center font-mono text-sm text-slate-900 font-black bg-slate-200/80">${st.validTotal}</td>
                <td class="py-1 px-2 text-center">
                  ${st.hasFailedSubject 
                    ? `<span class="text-[9px] font-bold text-rose-600 block leading-tight">Failed</span>` 
                    : `<span class="text-[9.5px] font-bold text-emerald-700">PASSED</span>`}
                </td>
              </tr>
            </tfoot>
          </table>

          ${st.hasFailedSubject ? `
            <div class="mt-0.5 px-2 py-0.5 bg-rose-50 border border-rose-200 rounded text-[8.5px] text-rose-800 leading-tight">
              <strong>* Rule Notice:</strong> As per policy, marks of failed subject(s) &lt;40% are excluded from Total: ${st.failedSubjects.map(f => `${f.title} (${f.mark}/${f.maxMarks})`).join(', ')}.
            </div>
          ` : ''}
        </div>

        <!-- 5 KPI Cards: Percentage, Grade, Position, Attendance, Remarks -->
        <div class="mt-1 pt-1 border-t border-slate-300">
          <div class="grid grid-cols-5 gap-1 text-center">
            <div class="border border-slate-200 rounded p-1 bg-slate-50">
              <span class="block text-[8px] uppercase text-slate-500 font-bold">Percentage</span>
              <span class="font-black text-xs font-mono text-slate-900">${st.percentage}%</span>
            </div>
            <div class="border border-slate-200 rounded p-1 bg-slate-50">
              <span class="block text-[8px] uppercase text-slate-500 font-bold">Grade</span>
              <span class="font-black text-xs px-1 rounded ${st.badgeClass}">${st.grade}</span>
            </div>
            <div class="border border-slate-200 rounded p-1 bg-slate-50">
              <span class="block text-[8px] uppercase text-slate-500 font-bold">Position</span>
              <span class="font-bold text-xs font-mono text-slate-800">${getOrdinal(st.position)}</span>
            </div>
            <div class="border border-slate-200 rounded p-1 bg-slate-50">
              <span class="block text-[8px] uppercase text-slate-500 font-bold">Attendance</span>
              <div class="font-mono text-xs font-bold text-slate-800 pt-0.5">
                <span class="border-b border-slate-400 inline-block w-5 text-center">&nbsp;</span> / <span class="border-b border-slate-400 inline-block w-5 text-center">&nbsp;</span>
              </div>
            </div>
            <div class="border border-slate-200 rounded p-1 bg-slate-50">
              <span class="block text-[8px] uppercase text-slate-500 font-bold">Remarks</span>
              <span class="font-bold text-[11px] text-slate-800 truncate block">${st.remarks}</span>
            </div>
          </div>
        </div>

        <!-- Official Signatures: Controller of Examinations & Dr. Shaukat Aziz (Principal) -->
        <div class="mt-1.5 pt-1 border-t border-slate-300">
          <div class="grid grid-cols-2 gap-12 text-center text-xs pt-1 text-slate-700">
            <div class="border-t border-slate-400 pt-0.5">
              <span class="font-semibold block text-slate-300">&nbsp;</span>
              <span class="text-[8.5px] text-slate-500 uppercase font-bold">Controller of Examinations</span>
            </div>
            <div class="border-t border-slate-400 pt-0.5">
              <span class="font-black block text-slate-900">${classData.meta.principal}</span>
              <span class="text-[8.5px] text-slate-500 uppercase font-bold">Principal</span>
            </div>
          </div>
        </div>

      </div>
    `;
  }

  function renderAllCards() {
    const rawData = (typeof CLASS_DATA !== 'undefined') ? CLASS_DATA : (typeof CLASS_7TH_BOYS_DATA !== 'undefined' ? CLASS_7TH_BOYS_DATA : null);
    if (!rawData) {
      console.error("No class data loaded from data.js");
      return;
    }
    const classData = processClass(rawData);
    const container = document.getElementById('cards-container');
    container.innerHTML = '';

    for (let i = 0; i < classData.students.length; i += 2) {
      const st1 = classData.students[i];
      const st2 = classData.students[i + 1];
      const pageNum = Math.floor(i / 2) + 1;

      const pageEl = document.createElement('div');
      pageEl.className = 'landscape-sheet bg-white rounded-lg shadow-sm border border-slate-200 relative mb-6 mx-auto';
      
      pageEl.innerHTML = `
        <div class="cards-row">
          <!-- Card 1 -->
          <div class="card-wrapper">
            ${renderResultCard(st1, classData)}
          </div>
          
          <!-- Center Cutting Gutter (Width: 28px, Symmetrically Centered) -->
          <div class="cutter-gutter">
            <div class="flex flex-col items-center text-xs">
              <span>✂</span>
              <span class="text-[7.5px] font-mono uppercase tracking-widest text-slate-400 font-bold mt-0.5">CUT</span>
            </div>
            <div class="cutter-line"></div>
            <div class="flex flex-col items-center text-xs">
              <span class="text-[7.5px] font-mono uppercase tracking-widest text-slate-400 font-bold mb-0.5">CUT</span>
              <span>✂</span>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="card-wrapper">
            ${st2 ? renderResultCard(st2, classData) : '<div class="card-box border-2 border-dashed border-slate-200 rounded-lg flex items-center justify-center text-slate-400 font-medium">End of Class Roster</div>'}
          </div>
        </div>

        <div class="no-print mt-1 text-right text-[10px] text-slate-400 font-medium">
          Page ${pageNum} of 8 &bull; Landscape Print (2 Students Per Sheet)
        </div>
      `;
      container.appendChild(pageEl);
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    renderAllCards();
    window.addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'p') {
        e.preventDefault();
        window.print();
      }
    });
  });
  </script>
</body>
</html>
"""

# =========================================================================
# 2. CONSOLIDATED MARKSHEET TEMPLATE
# =========================================================================
marksheet_tpl = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>7th Boys - Consolidated Mark Sheet 2nd Term 2026-27</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: 'Inter', sans-serif;
      -webkit-font-smoothing: antialiased;
      background-color: #f1f5f9;
    }
    .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }
    .logo-sharp {
      image-rendering: -webkit-optimize-contrast;
      image-rendering: crisp-edges;
    }
    @page {
      size: 297mm 210mm;
      margin: 0;
    }
    @media print {
      html, body {
        width: 297mm !important;
        height: 210mm !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #ffffff !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
        overflow: hidden !important;
      }
      .no-print {
        display: none !important;
      }
      .marksheet-container {
        padding: 0 !important;
        margin: 0 auto !important;
        max-width: none !important;
        width: 297mm !important;
        height: 210mm !important;
      }
      .marksheet-page {
        width: 297mm !important;
        height: 210mm !important;
        max-height: 210mm !important;
        page-break-after: avoid !important;
        page-break-inside: avoid !important;
        break-after: avoid !important;
        break-inside: avoid !important;
        margin: 0 !important;
        padding: 4mm 6mm !important;
        box-sizing: border-box !important;
        border: none !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        overflow: hidden !important;
      }
    }
    @media screen {
      .marksheet-container {
        padding: 1rem;
        max-width: 1240px;
        margin: 0 auto;
      }
    }
    .navbar-container {
      width: 100%;
      background: rgba(255, 255, 255, 0.98);
      border-bottom: 1px solid #e2e8f0;
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    }
  </style>
</head>
<body class="bg-slate-100 text-slate-900">

  <!-- Print Navigation Bar -->
  <div class="no-print navbar-container">
    <div class="flex items-center space-x-3" style="display: flex; align-items: center; gap: 12px;">
      <img src="logo.jpg" onerror="this.src=SCHOOL_LOGO_BASE64; this.onerror=null;" alt="School Logo" class="h-10 w-10 object-contain logo-sharp border border-slate-300 rounded-full" style="width: 40px; height: 40px; object-fit: contain; border-radius: 9999px;">
      <div>
        <h1 class="text-sm font-bold text-slate-800" style="font-size: 14px; font-weight: 700; color: #1e293b; margin: 0;">Al Rehman Public Secondary School Sadwal (Chakwal)</h1>
        <p class="text-xs text-slate-500" style="font-size: 12px; color: #64748b; margin: 0;">Consolidated Mark Sheet &bull; 7th Boys &bull; 2nd Term 2026-27</p>
      </div>
    </div>
    <div class="flex items-center space-x-3" style="display: flex; align-items: center; gap: 12px;">
      <a href="../../index.html" class="inline-flex items-center px-3 py-1.5 text-xs font-medium text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-md border border-slate-300 transition" style="display: inline-flex; align-items: center; padding: 6px 12px; font-size: 12px; font-weight: 500; color: #334155; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none;">
        &larr; Master Hub
      </a>
      <a href="cards.html" class="inline-flex items-center px-3 py-1.5 text-xs font-medium text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-md border border-slate-300 transition" style="display: inline-flex; align-items: center; padding: 6px 12px; font-size: 12px; font-weight: 500; color: #334155; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none;">
        Student Result Cards (2-per-page)
      </a>
      <a href="failure_sheet.html" class="inline-flex items-center px-3 py-1.5 text-xs font-medium text-rose-700 bg-rose-50 hover:bg-rose-100 rounded-md border border-rose-200 transition" style="display: inline-flex; align-items: center; padding: 6px 12px; font-size: 12px; font-weight: 500; color: #be123c; background: #fff1f2; border: 1px solid #fecdd3; border-radius: 6px; text-decoration: none;">
        Failure Sheet
      </a>
      <button onclick="window.print()" class="inline-flex items-center space-x-1.5 bg-slate-900 hover:bg-slate-800 text-white text-xs font-semibold px-4 py-2 rounded-md shadow transition cursor-pointer" style="display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; font-size: 12px; font-weight: 600; color: #ffffff; background: #0f172a; border: none; border-radius: 6px; cursor: pointer;">
        <svg class="w-4 h-4" style="width: 16px; height: 16px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
        <span>Print Mark Sheet (Ctrl+P)</span>
      </button>
    </div>
  </div>

  <div class="marksheet-container">
    <div class="marksheet-page bg-white p-3.5 rounded-lg shadow-sm border border-slate-200 flex flex-col justify-between">
      
      <!-- Header -->
      <div class="border-b-[1.5px] border-slate-800 pb-2">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3.5">
            <img src="logo.jpg" onerror="this.src=SCHOOL_LOGO_BASE64; this.onerror=null;" alt="Logo" class="h-14 w-14 object-contain logo-sharp">
            <div>
              <h1 class="text-base font-black tracking-tight text-slate-900 uppercase leading-none">
                Al Rehman Public Secondary School Sadwal (Chakwal)
              </h1>
              <div class="flex items-center space-x-2 text-[10.5px] text-slate-600 mt-1 font-medium">
                <span>Sadwal, Chakwal</span>
                <span>&bull;</span>
                <span class="italic font-serif">"Enter to Learn - Leave to Serve"</span>
                <span>&bull;</span>
                <span class="font-bold text-slate-800">Session 2026-27</span>
              </div>
            </div>
          </div>
          <div class="text-right">
            <span class="inline-block bg-slate-900 text-white font-extrabold text-xs px-3 py-1 rounded shadow-sm tracking-wide uppercase">
              Consolidated Award List &bull; 2nd Term
            </span>
            <div class="text-[10.5px] text-slate-600 mt-1">
              Class: <strong class="text-slate-900">7th Boys</strong> | Incharge: <strong class="text-slate-900">Laiba Batool</strong> | Max: <strong class="text-slate-900 font-mono">435</strong>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick KPI Stats Bar -->
      <div class="grid grid-cols-5 gap-2 my-2 text-center text-xs">
        <div class="bg-slate-50 border border-slate-200 rounded p-1.5">
          <span class="block text-[9px] uppercase font-semibold text-slate-500">Total Enrolled</span>
          <span class="font-bold text-slate-900 font-mono text-sm">16 Students</span>
        </div>
        <div class="bg-slate-50 border border-slate-200 rounded p-1.5">
          <span class="block text-[9px] uppercase font-semibold text-slate-500">Passing Standard</span>
          <span class="font-bold text-slate-900 text-sm">40% (Boys Section)</span>
        </div>
        <div class="bg-slate-50 border border-slate-200 rounded p-1.5">
          <span class="block text-[9px] uppercase font-semibold text-slate-500">Class Average</span>
          <span class="font-bold text-slate-900 font-mono text-sm" id="class-avg">&mdash;</span>
        </div>
        <div class="bg-emerald-50 border border-emerald-200 rounded p-1.5">
          <span class="block text-[9px] uppercase font-semibold text-emerald-700">1st Position Holder</span>
          <span class="font-bold text-emerald-900 text-sm" id="first-pos">&mdash;</span>
        </div>
        <div class="bg-blue-50 border border-blue-200 rounded p-1.5">
          <span class="block text-[9px] uppercase font-semibold text-blue-700">Policy Standard</span>
          <span class="font-semibold text-blue-900 text-[10.5px]">Failed Marks Excluded</span>
        </div>
      </div>

      <!-- Consolidated Table with LARGER FONT (text-xs / 12px) -->
      <div class="flex-1 overflow-hidden">
        <table class="w-full text-left border-collapse border border-slate-300 text-xs">
          <thead>
            <tr class="bg-slate-800 text-white font-bold uppercase text-[10px] tracking-wider text-center">
              <th class="py-1 px-1 border-r border-slate-700 w-7">Sr</th>
              <th class="py-1 px-2 border-r border-slate-700 text-left w-36">Student Name</th>
              <th class="py-1 px-1 border-r border-slate-700">Eng</th>
              <th class="py-1 px-1 border-r border-slate-700">Urdu</th>
              <th class="py-1 px-1 border-r border-slate-700">Math</th>
              <th class="py-1 px-1 border-r border-slate-700">Sci</th>
              <th class="py-1 px-1 border-r border-slate-700">Comp</th>
              <th class="py-1 px-1 border-r border-slate-700">Al-Q</th>
              <th class="py-1 px-1 border-r border-slate-700">Isl</th>
              <th class="py-1 px-1 border-r border-slate-700">Draw</th>
              <th class="py-1 px-1 border-r border-slate-700">Model</th>
              <th class="py-1 px-1 border-r border-slate-700">Al-Q(O)</th>
              <th class="py-1 px-1 border-r border-slate-700">Oral</th>
              <th class="py-1 px-1 border-r border-slate-700">His</th>
              <th class="py-1 px-2 border-r border-slate-700 bg-slate-900 text-amber-300 font-extrabold">Total</th>
              <th class="py-1 px-1.5 border-r border-slate-700 bg-slate-900 text-amber-300 font-extrabold">%age</th>
              <th class="py-1 px-1 border-r border-slate-700">Grade</th>
              <th class="py-1 px-1.5 border-r border-slate-700">Pos</th>
              <th class="py-1 px-2 text-left">Teacher Remarks</th>
            </tr>
            <tr class="bg-slate-200 text-slate-700 font-semibold text-[9.5px] text-center border-b border-slate-400">
              <td colspan="2" class="py-0.5 px-2 text-left font-bold uppercase">Maximum Marks &rarr;</td>
              <td class="py-0.5 px-1 font-mono">50</td>
              <td class="py-0.5 px-1 font-mono">50</td>
              <td class="py-0.5 px-1 font-mono">50</td>
              <td class="py-0.5 px-1 font-mono">50</td>
              <td class="py-0.5 px-1 font-mono">50</td>
              <td class="py-0.5 px-1 font-mono">50</td>
              <td class="py-0.5 px-1 font-mono">50</td>
              <td class="py-0.5 px-1 font-mono">10</td>
              <td class="py-0.5 px-1 font-mono">5</td>
              <td class="py-0.5 px-1 font-mono">10</td>
              <td class="py-0.5 px-1 font-mono">10</td>
              <td class="py-0.5 px-1 font-mono">50</td>
              <td class="py-0.5 px-2 font-mono font-bold bg-slate-300 text-slate-900">435</td>
              <td class="py-0.5 px-1.5 font-mono">100%</td>
              <td colspan="3" class="py-0.5 px-1 text-slate-500">Pass Mark: 40%</td>
            </tr>
          </thead>
          <tbody id="table-body">
            <!-- Populated via JavaScript -->
          </tbody>
        </table>
      </div>

      <!-- Grading Scale Legend & Rule Footnote -->
      <div class="mt-2 pt-1 border-t border-slate-300">
        <div class="flex items-center justify-between text-[9px] bg-slate-50 p-1.5 rounded border border-slate-200 text-slate-700">
          <div class="space-x-1">
            <span class="font-bold text-slate-900 uppercase">Grading Scale:</span>
            <span>&le;100%: <strong class="text-emerald-700">A+</strong> (Excellent)</span> &bull;
            <span>&le;90%: <strong class="text-blue-700">A</strong> (Very Good)</span> &bull;
            <span>&le;80%: <strong class="text-sky-700">B</strong> (Good)</span> &bull;
            <span>&le;70%: <strong class="text-amber-700">C</strong> (Satisfactory)</span> &bull;
            <span>&le;60%: <strong class="text-orange-700">D</strong> (Work Hard)</span> &bull;
            <span>&le;50%: <strong class="text-purple-700">E</strong> (Poor)</span> &bull;
            <span>&lt;40%: <strong class="text-rose-700">F</strong> (Fail)</span>
          </div>
          <div class="font-semibold text-rose-700">
            * Marks with red background failed (&lt;40%) and are EXCLUDED from the Total Marks.
          </div>
        </div>
      </div>

      <!-- Signatures Row: Principal Dr. Shaukat Aziz -->
      <div class="mt-2 pt-1 border-t border-slate-300">
        <div class="grid grid-cols-3 gap-8 text-center text-[10px] pt-1.5 text-slate-700">
          <div class="border-t border-slate-400 pt-0.5">
            <span class="font-bold block text-slate-900">Laiba Batool</span>
            <span class="text-[8.5px] text-slate-400 uppercase">Class Incharge (7th Boys)</span>
          </div>
          <div class="border-t border-slate-400 pt-0.5">
            <span class="font-semibold block text-slate-300">&nbsp;</span>
            <span class="text-[8.5px] text-slate-400 uppercase">Controller of Examinations</span>
          </div>
          <div class="border-t border-slate-400 pt-0.5">
            <span class="font-bold block text-slate-900">Dr. Shaukat Aziz</span>
            <span class="text-[8.5px] text-slate-500 uppercase font-semibold">Principal</span>
          </div>
        </div>
      </div>

    </div>
  </div>

  __SCRIPTS__

  <script>
  function renderTable() {
    const rawData = (typeof CLASS_DATA !== 'undefined') ? CLASS_DATA : (typeof CLASS_7TH_BOYS_DATA !== 'undefined' ? CLASS_7TH_BOYS_DATA : null);
    if (!rawData) {
      console.error("No class data loaded from data.js");
      return;
    }
    const classData = processClass(rawData);
    const tbody = document.getElementById('table-body');
    tbody.innerHTML = '';

    document.getElementById('class-avg').textContent = `${classData.meta.classAveragePct}%`;
    document.getElementById('first-pos').textContent = `${classData.meta.topStudent.name} (${classData.meta.topStudent.validTotal})`;

    classData.students.forEach((st, idx) => {
      const isTop3 = st.position <= 3;
      const rowBg = st.hasFailedSubject 
        ? 'bg-amber-50/50 hover:bg-amber-100/60' 
        : (isTop3 ? 'bg-emerald-50/40 font-medium' : (idx % 2 === 0 ? 'bg-white' : 'bg-slate-50/70'));

      const positionBadge = st.position === 1 ? `<span class="bg-amber-100 text-amber-900 font-bold px-1.5 py-0.2 rounded text-[9px] border border-amber-300">1st</span>`
        : st.position === 2 ? `<span class="bg-slate-200 text-slate-800 font-bold px-1.5 py-0.2 rounded text-[9px] border border-slate-400">2nd</span>`
        : st.position === 3 ? `<span class="bg-amber-50 text-amber-800 font-bold px-1.5 py-0.2 rounded text-[9px] border border-amber-200">3rd</span>`
        : `<span class="text-slate-600 font-mono text-xs">${getOrdinal(st.position)}</span>`;

      // Subject cells with LARGER font (text-xs)
      const cells = st.subjectResults.map(sub => {
        if (!sub.isPass) {
          return `<td class="py-1 px-1 text-center font-mono font-bold bg-rose-100/90 text-rose-700 border-x border-rose-300 text-xs" title="Failed: ${sub.mark}/${sub.maxMarks} (<40%)">${sub.mark}*</td>`;
        }
        return `<td class="py-1 px-1 text-center font-mono text-slate-800 border-x border-slate-200 text-xs">${sub.mark}</td>`;
      }).join('');

      // Clean Total column (valid total ONLY)
      const tr = document.createElement('tr');
      tr.className = `${rowBg} border-b border-slate-200 text-xs transition hover:bg-slate-100/60`;
      tr.innerHTML = `
        <td class="py-1 px-1 text-center text-slate-400 font-mono text-[10px] border-r border-slate-200">${st.sr}</td>
        <td class="py-1 px-2 text-slate-900 font-semibold border-r border-slate-200 whitespace-nowrap text-xs">${st.name}</td>
        ${cells}
        <td class="py-1 px-2 text-center font-mono font-extrabold text-slate-900 bg-slate-100 border-x border-slate-300 text-xs">
          ${st.validTotal}
        </td>
        <td class="py-1 px-1.5 text-center font-mono font-bold text-slate-800 border-r border-slate-200 text-xs">${st.percentage}%</td>
        <td class="py-1 px-1 text-center border-r border-slate-200">
          <span class="font-bold px-1.5 py-0.2 rounded text-[9.5px] ${st.badgeClass}">${st.grade}</span>
        </td>
        <td class="py-1 px-1.5 text-center border-r border-slate-200 font-semibold">${positionBadge}</td>
        <td class="py-1 px-2 text-slate-700 font-medium whitespace-nowrap text-xs">${st.remarks}</td>
      `;
      tbody.appendChild(tr);
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    renderTable();
    window.addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'p') {
        e.preventDefault();
        window.print();
      }
    });
  });
  </script>
</body>
</html>
"""

# =========================================================================
# 3. FAILURE SHEET TEMPLATE
# =========================================================================
failure_tpl = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>7th Boys - Failure & Compartment Sheet 2nd Term 2026-27</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: 'Inter', sans-serif;
      -webkit-font-smoothing: antialiased;
      background-color: #f1f5f9;
    }
    .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }
    .logo-sharp {
      image-rendering: -webkit-optimize-contrast;
      image-rendering: crisp-edges;
    }
    @page {
      size: 297mm 210mm;
      margin: 0;
    }
    @media print {
      html, body {
        width: 297mm !important;
        height: 210mm !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #ffffff !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
        overflow: hidden !important;
      }
      .no-print {
        display: none !important;
      }
      .failure-container {
        padding: 0 !important;
        margin: 0 auto !important;
        max-width: none !important;
        width: 297mm !important;
        height: 210mm !important;
      }
      .failure-page {
        width: 297mm !important;
        height: 210mm !important;
        max-height: 210mm !important;
        page-break-after: avoid !important;
        page-break-inside: avoid !important;
        break-after: avoid !important;
        break-inside: avoid !important;
        margin: 0 !important;
        padding: 4mm 6mm !important;
        box-sizing: border-box !important;
        border: none !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        overflow: hidden !important;
      }
    }
    @media screen {
      .failure-container {
        padding: 1rem;
        max-width: 1240px;
        margin: 0 auto;
      }
    }
    .navbar-container {
      width: 100%;
      background: rgba(255, 255, 255, 0.98);
      border-bottom: 1px solid #e2e8f0;
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    }
  </style>
</head>
<body class="bg-slate-100 text-slate-900">

  <!-- Print Navigation Bar -->
  <div class="no-print navbar-container">
    <div class="flex items-center space-x-3" style="display: flex; align-items: center; gap: 12px;">
      <img src="logo.jpg" onerror="this.src=SCHOOL_LOGO_BASE64; this.onerror=null;" alt="School Logo" class="h-10 w-10 object-contain logo-sharp border border-slate-300 rounded-full" style="width: 40px; height: 40px; object-fit: contain; border-radius: 9999px;">
      <div>
        <h1 class="text-sm font-bold text-slate-800" style="font-size: 14px; font-weight: 700; color: #1e293b; margin: 0;">Al Rehman Public Secondary School Sadwal (Chakwal)</h1>
        <p class="text-xs text-rose-600 font-semibold" style="font-size: 12px; color: #e11d48; margin: 0;">Official Failure & Compartment Award List &bull; 7th Boys</p>
      </div>
    </div>
    <div class="flex items-center space-x-3" style="display: flex; align-items: center; gap: 12px;">
      <a href="../../index.html" class="inline-flex items-center px-3 py-1.5 text-xs font-medium text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-md border border-slate-300 transition" style="display: inline-flex; align-items: center; padding: 6px 12px; font-size: 12px; font-weight: 500; color: #334155; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none;">
        &larr; Master Hub
      </a>
      <a href="marksheet.html" class="inline-flex items-center px-3 py-1.5 text-xs font-medium text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-md border border-slate-300 transition" style="display: inline-flex; align-items: center; padding: 6px 12px; font-size: 12px; font-weight: 500; color: #334155; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none;">
        Consolidated Sheet
      </a>
      <a href="cards.html" class="inline-flex items-center px-3 py-1.5 text-xs font-medium text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-md border border-slate-300 transition" style="display: inline-flex; align-items: center; padding: 6px 12px; font-size: 12px; font-weight: 500; color: #334155; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none;">
        Result Cards (2-per-page)
      </a>
      <button onclick="window.print()" class="inline-flex items-center space-x-1.5 bg-rose-700 hover:bg-rose-800 text-white text-xs font-semibold px-4 py-2 rounded-md shadow transition cursor-pointer" style="display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; font-size: 12px; font-weight: 600; color: #ffffff; background: #be123c; border: none; border-radius: 6px; cursor: pointer;">
        <svg class="w-4 h-4" style="width: 16px; height: 16px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
        <span>Print Failure Sheet (Ctrl+P)</span>
      </button>
    </div>
  </div>

  <div class="failure-container">
    <div class="failure-page bg-white p-4 rounded-lg shadow-sm border border-slate-200 flex flex-col justify-between">
      
      <!-- Header -->
      <div class="border-b-[1.5px] border-slate-800 pb-2">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3.5">
            <img src="logo.jpg" onerror="this.src=SCHOOL_LOGO_BASE64; this.onerror=null;" alt="Logo" class="h-14 w-14 object-contain logo-sharp">
            <div>
              <h1 class="text-base font-black tracking-tight text-slate-900 uppercase leading-none">
                Al Rehman Public Secondary School Sadwal (Chakwal)
              </h1>
              <div class="flex items-center space-x-2 text-[10.5px] text-slate-600 mt-1 font-medium">
                <span>Sadwal, Chakwal</span>
                <span>&bull;</span>
                <span class="italic font-serif">"Enter to Learn - Leave to Serve"</span>
                <span>&bull;</span>
                <span class="font-bold text-slate-800">Academic Session 2026-27</span>
              </div>
            </div>
          </div>
          <div class="text-right">
            <span class="inline-block bg-rose-700 text-white font-extrabold text-xs px-3 py-1 rounded shadow-sm tracking-wide uppercase">
              Failure & Compartment List &bull; 2nd Term
            </span>
            <div class="text-[10.5px] text-slate-600 mt-1">
              Class: <strong class="text-slate-900">7th Boys</strong> | Passing Standard: <strong class="text-rose-700">40%</strong> | Principal: <strong class="text-slate-900">Dr. Shaukat Aziz</strong>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick KPI Stats Bar -->
      <div class="grid grid-cols-4 gap-3 my-3 text-center text-xs">
        <div class="bg-slate-50 border border-slate-200 rounded p-2">
          <span class="block text-[9.5px] uppercase font-semibold text-slate-500">Total Class Strength</span>
          <span class="font-bold text-slate-900 font-mono text-base">16 Students</span>
        </div>
        <div class="bg-emerald-50 border border-emerald-200 rounded p-2">
          <span class="block text-[9.5px] uppercase font-semibold text-emerald-700">Passed in All Subjects</span>
          <span class="font-bold text-emerald-900 font-mono text-base" id="passed-count">14 Students (87.50%)</span>
        </div>
        <div class="bg-rose-50 border border-rose-200 rounded p-2">
          <span class="block text-[9.5px] uppercase font-semibold text-rose-700">Students with Failures</span>
          <span class="font-bold text-rose-900 font-mono text-base" id="failed-count">2 Students</span>
        </div>
        <div class="bg-amber-50 border border-amber-200 rounded p-2">
          <span class="block text-[9.5px] uppercase font-semibold text-amber-700">Excluded Marks Policy</span>
          <span class="font-bold text-amber-900 text-xs">Failed Marks Excluded from Total</span>
        </div>
      </div>

      <!-- Failure Students Table -->
      <div class="flex-1 overflow-hidden">
        <table class="w-full text-left border-collapse border border-slate-300 text-xs">
          <thead>
            <tr class="bg-slate-800 text-white font-bold uppercase text-[10.5px] tracking-wider text-center">
              <th class="py-2 px-2 border-r border-slate-700 w-12">Sr #</th>
              <th class="py-2 px-2 border-r border-slate-700 w-16">Roll #</th>
              <th class="py-2 px-3 border-r border-slate-700 text-left w-48">Student Name</th>
              <th class="py-2 px-3 border-r border-slate-700 text-left">Failed Subject(s) & Marks</th>
              <th class="py-2 px-2 border-r border-slate-700 w-24">Failed Subs</th>
              <th class="py-2 px-2 border-r border-slate-700 w-28">Excluded Marks</th>
              <th class="py-2 px-2 border-r border-slate-700 w-24">Valid Total</th>
              <th class="py-2 px-2 border-r border-slate-700 w-20">%age</th>
              <th class="py-2 px-2 border-r border-slate-700 w-16">Grade</th>
              <th class="py-2 px-3 text-left w-36">Remarks</th>
            </tr>
          </thead>
          <tbody id="failure-tbody">
            <!-- Populated via JavaScript -->
          </tbody>
        </table>
      </div>

      <!-- Remedial Policy Footnote -->
      <div class="mt-3 pt-2 border-t border-slate-300">
        <div class="bg-rose-50 border border-rose-200 rounded p-2 text-[10px] text-rose-900 flex items-center justify-between">
          <div>
            <strong>* Examination Academic Directive:</strong> Passing criteria for Boys section is 40%. The above students must appear in the <strong>2nd Term Compartment & Remedial Re-Tests</strong> for the specific subjects indicated above.
          </div>
          <div class="font-semibold text-rose-700 whitespace-nowrap pl-4">
            Al Rehman Public Secondary School Sadwal
          </div>
        </div>
      </div>

      <!-- Official Signatures: Class Incharge, Controller, and Dr. Shaukat Aziz (Principal) -->
      <div class="mt-3 pt-1 border-t border-slate-300">
        <div class="grid grid-cols-3 gap-12 text-center text-xs pt-2 text-slate-700">
          <div class="border-t border-slate-400 pt-1">
            <span class="font-bold block text-slate-900">Laiba Batool</span>
            <span class="text-[9.5px] text-slate-500 uppercase font-semibold">Class Incharge (7th Boys)</span>
          </div>
          <div class="border-t border-slate-400 pt-1">
            <span class="font-semibold block text-slate-300">&nbsp;</span>
            <span class="text-[9.5px] text-slate-500 uppercase font-semibold">Controller of Examinations</span>
          </div>
          <div class="border-t border-slate-400 pt-1">
            <span class="font-bold block text-slate-900">Dr. Shaukat Aziz</span>
            <span class="text-[9.5px] text-slate-500 uppercase font-semibold">Principal</span>
          </div>
        </div>
      </div>

    </div>
  </div>

  __SCRIPTS__

  <script>
  function renderFailureSheet() {
    const rawData = (typeof CLASS_DATA !== 'undefined') ? CLASS_DATA : (typeof CLASS_7TH_BOYS_DATA !== 'undefined' ? CLASS_7TH_BOYS_DATA : null);
    if (!rawData) {
      console.error("No class data loaded from data.js");
      return;
    }
    const classData = processClass(rawData);
    const tbody = document.getElementById('failure-tbody');
    tbody.innerHTML = '';

    const failed = classData.failedStudents;
    const passedCount = classData.students.length - failed.length;
    const passedPct = ((passedCount / classData.students.length) * 100).toFixed(2);
    document.getElementById('failed-count').textContent = `${failed.length} Students`;
    const passedEl = document.getElementById('passed-count');
    if (passedEl) {
      passedEl.textContent = `${passedCount} Students (${passedPct}%)`;
    }

    if (failed.length === 0) {
      tbody.innerHTML = '<tr><td colspan="10" class="py-8 text-center text-emerald-700 font-bold text-sm bg-emerald-50">All students passed in all subjects!</td></tr>';
      return;
    }

    failed.forEach((st, idx) => {
      const tr = document.createElement('tr');
      tr.className = 'border-b border-slate-200 text-xs hover:bg-rose-50/40 transition';

      const failedSubsHtml = st.failedSubjects.map(sub => `
        <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-bold bg-rose-100 text-rose-800 border border-rose-300 mr-1.5 my-0.5">
          ${sub.title}: <strong class="ml-1 text-rose-950">${sub.mark}/${sub.maxMarks}</strong>
          <span class="ml-1 text-[9px] text-rose-600 font-normal">(Min: ${sub.passingMin})</span>
        </span>
      `).join('');

      tr.innerHTML = `
        <td class="py-2.5 px-2 text-center text-slate-500 font-mono border-r border-slate-200 font-semibold">${idx + 1}</td>
        <td class="py-2.5 px-2 text-center font-mono text-slate-900 font-bold border-r border-slate-200">#${String(st.rollNo).padStart(2, '0')}</td>
        <td class="py-2.5 px-3 font-bold text-slate-900 border-r border-slate-200">${st.name}</td>
        <td class="py-2.5 px-3 border-r border-slate-200 leading-normal">${failedSubsHtml}</td>
        <td class="py-2.5 px-2 text-center font-bold text-rose-700 border-r border-slate-200 font-mono">${st.failedSubjects.length} Sub(s)</td>
        <td class="py-2.5 px-2 text-center font-mono text-rose-700 font-bold border-r border-slate-200 bg-rose-50/50">${st.excludedMarks} Marks</td>
        <td class="py-2.5 px-2 text-center font-mono font-black text-slate-900 border-r border-slate-200 bg-slate-100">${st.validTotal}</td>
        <td class="py-2.5 px-2 text-center font-mono font-bold text-slate-800 border-r border-slate-200">${st.percentage}%</td>
        <td class="py-2.5 px-2 text-center border-r border-slate-200">
          <span class="font-bold px-1.5 py-0.2 rounded text-[10px] ${st.badgeClass}">${st.grade}</span>
        </td>
        <td class="py-2.5 px-3 font-medium text-slate-700">${st.remarks}</td>
      `;
      tbody.appendChild(tr);
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    renderFailureSheet();
    window.addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'p') {
        e.preventDefault();
        window.print();
      }
    });
  });
  </script>
</body>
</html>
"""

# =========================================================================
# 4. MASTER HUB (index.html)
# =========================================================================
index_tpl = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Al Rehman Public Secondary School - Academic Examination Portal</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Inter', sans-serif; -webkit-font-smoothing: antialiased; }
    .font-mono { font-family: 'JetBrains Mono', monospace; }
    .logo-sharp { image-rendering: -webkit-optimize-contrast; image-rendering: crisp-edges; }
  </style>
</head>
<body class="bg-slate-50 text-slate-900 min-h-screen">

  <header class="bg-white border-b border-slate-200 sticky top-0 z-50 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center space-x-3.5">
          <img src="logo.jpg" onerror="this.src=SCHOOL_LOGO_BASE64; this.onerror=null;" alt="School Logo" class="h-12 w-12 object-contain logo-sharp border border-slate-300 rounded-full shadow-sm">
          <div>
            <div class="flex items-center space-x-2">
              <h1 class="text-base font-bold text-slate-900 leading-tight">
                Al Rehman Public Secondary School Sadwal
              </h1>
              <span class="bg-slate-100 text-slate-700 text-xs font-semibold px-2 py-0.5 rounded border border-slate-300">Chakwal</span>
            </div>
            <p class="text-xs text-slate-500">2nd Term Examination 2026-27 &bull; Principal: <strong class="text-slate-700 font-semibold">Dr. Shaukat Aziz</strong></p>
          </div>
        </div>
        <div class="flex items-center space-x-2">
          <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800 border border-emerald-300">
            &bull; Academic Session 2026-27
          </span>
        </div>
      </div>
    </div>
  </header>

  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
    <div class="bg-slate-900 text-white rounded-xl p-6 shadow-md relative overflow-hidden">
      <div class="relative z-10 max-w-2xl">
        <span class="inline-block bg-amber-400 text-slate-900 font-bold text-xs uppercase px-2.5 py-0.5 rounded-full mb-2">
          Enter to Learn &mdash; Leave to Serve
        </span>
        <h2 class="text-2xl font-black tracking-tight">Academic Result Generation & Printing Hub</h2>
        <p class="text-slate-300 text-sm mt-1">
          Generate consolidated mark sheets, failure sheets, and landscape student result cards (2 per page) with automated grade calculation and policy enforcement.
        </p>
      </div>
      <div class="absolute right-4 bottom-2 opacity-10 pointer-events-none">
        <img src="logo.jpg" onerror="this.src=SCHOOL_LOGO_BASE64; this.onerror=null;" alt="Watermark" class="w-48 h-48 logo-sharp">
      </div>
    </div>

    <div>
      <div class="flex items-center justify-between mb-4">
        <div>
          <h3 class="text-lg font-bold text-slate-900">Class Results Directory</h3>
          <p class="text-xs text-slate-500">Select a class below to generate mark sheets or print landscape student cards</p>
        </div>
        <div class="text-xs text-slate-500 bg-white border border-slate-200 px-3 py-1.5 rounded-md shadow-sm">
          Principal: <strong>Dr. Shaukat Aziz</strong>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="bg-white border-2 border-slate-800 rounded-xl p-5 shadow-sm hover:shadow-md transition flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between">
              <span class="bg-blue-100 text-blue-800 text-xs font-bold px-2.5 py-0.5 rounded border border-blue-300">
                Boys Section
              </span>
              <span class="text-xs font-semibold text-slate-500">40% Pass Standard</span>
            </div>
            
            <h4 class="text-xl font-black text-slate-900 mt-2">7th Boys</h4>
            <p class="text-xs text-slate-500 mt-0.5">Principal: <strong class="text-slate-700">Dr. Shaukat Aziz</strong></p>

            <div class="grid grid-cols-3 gap-2 mt-4 pt-3 border-t border-slate-100 text-center text-xs">
              <div class="bg-slate-50 p-2 rounded">
                <span class="block text-[10px] text-slate-400 font-semibold uppercase">Students</span>
                <span class="font-bold text-slate-900 font-mono text-sm">16</span>
              </div>
              <div class="bg-slate-50 p-2 rounded">
                <span class="block text-[10px] text-slate-400 font-semibold uppercase">Average</span>
                <span class="font-bold text-slate-900 font-mono text-sm">84.7%</span>
              </div>
              <div class="bg-slate-50 p-2 rounded">
                <span class="block text-[10px] text-slate-400 font-semibold uppercase">Top Mark</span>
                <span class="font-bold text-emerald-700 font-mono text-sm">426</span>
              </div>
            </div>

            <div class="mt-3 text-[11px] text-slate-600 bg-amber-50 border border-amber-200 rounded p-2">
              <strong>Rules Applied:</strong> Failed marks (&lt;40%) excluded from totals. Incharge hidden on cards. Attendance card added with blank manual write-in space.
            </div>
          </div>

          <div class="mt-5 space-y-2 pt-3 border-t border-slate-100">
            <a href="classes/7th_boys/cards.html" class="w-full flex items-center justify-center space-x-2 bg-slate-900 hover:bg-slate-800 text-white text-xs font-semibold py-2.5 rounded-lg shadow transition">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
              <span>Print Student Cards (2 per page)</span>
            </a>
            <div class="grid grid-cols-2 gap-2">
              <a href="classes/7th_boys/marksheet.html" class="flex items-center justify-center text-center bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-semibold py-2 rounded-lg border border-slate-300 transition">
                <span>Consolidated Mark Sheet</span>
              </a>
              <a href="classes/7th_boys/failure_sheet.html" class="flex items-center justify-center text-center bg-rose-50 hover:bg-rose-100 text-rose-800 text-xs font-semibold py-2 rounded-lg border border-rose-200 transition">
                <span>Failure Sheet (2)</span>
              </a>
            </div>
          </div>
        </div>

        <div class="border-2 border-dashed border-slate-300 rounded-xl p-6 flex flex-col items-center justify-center text-center bg-slate-50/50">
          <div class="w-12 h-12 rounded-full bg-slate-200 flex items-center justify-center text-slate-400 text-xl font-bold mb-3">
            +
          </div>
          <h4 class="text-sm font-bold text-slate-700">Next Class Ready to Import</h4>
          <p class="text-xs text-slate-400 mt-1 max-w-xs">
            Provide the next mark sheet image or data and it will automatically generate in this format.
          </p>
        </div>

      </div>
    </div>

    <div class="bg-white border border-slate-200 rounded-xl p-5 shadow-sm">
      <h4 class="text-sm font-bold text-slate-900 uppercase tracking-wide mb-3">School Academic & Grading Guidelines</h4>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div class="space-y-1.5 text-slate-600 bg-slate-50 p-3 rounded-lg border border-slate-200">
          <span class="font-bold text-slate-900 block">Passing Standards:</span>
          <div>&bull; <strong>Section A</strong>: 70% minimum passing mark.</div>
          <div>&bull; <strong>Section B / Boys / Girls</strong>: 40% minimum passing mark.</div>
          <div>&bull; <strong>Failed Subject Policy</strong>: Marks obtained in failed subjects are strictly excluded from the student's Total Marks.</div>
        </div>
        <div class="space-y-1.5 text-slate-600 bg-slate-50 p-3 rounded-lg border border-slate-200">
          <span class="font-bold text-slate-900 block">Grading Scale & Teacher Remarks:</span>
          <div>&bull; <strong>&le; 100%</strong>: Grade <strong>A+</strong> | Remarks: <em>Excellent</em></div>
          <div>&bull; <strong>&le; 90%</strong>: Grade <strong>A</strong> | Remarks: <em>Very Good</em></div>
          <div>&bull; <strong>&le; 80%</strong>: Grade <strong>B</strong> | Remarks: <em>Good</em></div>
          <div>&bull; <strong>&le; 70%</strong>: Grade <strong>C</strong> | Remarks: <em>Satisfactory</em></div>
          <div>&bull; <strong>&le; 60%</strong>: Grade <strong>D</strong> | Remarks: <em>Work Hard</em></div>
          <div>&bull; <strong>&le; 50%</strong>: Grade <strong>E</strong> | Remarks: <em>Poor</em></div>
          <div>&bull; <strong>&lt; 40%</strong>: Grade <strong>F</strong> | Remarks: <em>Fail</em></div>
        </div>
      </div>
    </div>

  </main>
</body>
</html>
"""

# Replace tags
final_cards = cards_tpl.replace('__SCRIPTS__', EMBEDDED_SCRIPTS)
final_marksheet = marksheet_tpl.replace('__SCRIPTS__', EMBEDDED_SCRIPTS)
final_failure = failure_tpl.replace('__SCRIPTS__', EMBEDDED_SCRIPTS)
final_index = index_tpl

# Save to classes/7th_boys/
os.makedirs(os.path.join(BASE_DIR, 'classes', '7th_boys'), exist_ok=True)
with open(os.path.join(BASE_DIR, 'classes', '7th_boys', 'data.js'), 'w', encoding='utf-8') as f:
    f.write(class_7th_boys_js)
with open(os.path.join(BASE_DIR, 'classes', '7th_boys', 'cards.html'), 'w', encoding='utf-8') as f:
    f.write(final_cards)
with open(os.path.join(BASE_DIR, 'classes', '7th_boys', 'marksheet.html'), 'w', encoding='utf-8') as f:
    f.write(final_marksheet)
with open(os.path.join(BASE_DIR, 'classes', '7th_boys', 'failure_sheet.html'), 'w', encoding='utf-8') as f:
    f.write(final_failure)


# Save root hub
with open(os.path.join(BASE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(final_index)

print("Build completed successfully!")
