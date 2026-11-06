#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
pre=r'''\documentclass[10pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx,amsmath,amssymb,booktabs,hyperref}
\begin{document}
'''
(root/'preview/summary_check.tex').write_text(pre+r'\input{sections/00_summary}'+ '\n'+r'\bibliographystyle{plain}\bibliography{refs}\end{document}')
parts=[('Reproducibility Summary','00_summary'),('Introduction','01_intro'),('Scope of Reproducibility','02_scope'),('Methodology','03_methodology'),('Results','04_results'),('Beyond the paper','05_beyond'),('Discussion','06_discussion')]
s=pre
for title,file in parts:s+=(r'\section*{' if file=='00_summary' else r'\section{')+title+'}\n'+r'\input{sections/'+file+'}\n'
s+=r'\bibliographystyle{plain}\bibliography{refs}\end{document}'
(root/'preview/draft_check.tex').write_text(s)
