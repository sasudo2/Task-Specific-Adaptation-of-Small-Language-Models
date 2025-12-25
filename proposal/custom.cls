% custom.cls — IOE Thapathali guidelines

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{custom}[2025/12/21 IOE Thapathali Format]

% Base class
\LoadClass[12pt,a4paper]{report}

% Packages
\RequirePackage{geometry}
\RequirePackage{titlesec}
\RequirePackage{setspace}
\RequirePackage{xcolor}
\RequirePackage{newtxtext}   % Times-like text

\RequirePackage{fancyhdr}
\RequirePackage{etoolbox}
\RequirePackage{caption}
\RequirePackage{tocloft}
\RequirePackage{amsmath}     % Math support
\RequirePackage{pgfgantt}    % Gantt charts

% Page layout
\geometry{
  top=1in,
  bottom=1in,
  left=1.5in,
  right=1in,
  includefoot % allow precise footer placement
}
\setlength{\footskip}{0.5in} % page number 0.5" from bottom


% Headers/footers: centered page number at footer, no header line
\pagestyle{fancy}
\fancyhf{}
\cfoot{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Front matter and main matter helpers (Roman for prefatory, Arabic for body)
\newcommand{\frontmatter}{%
  \cleardoublepage
  \pagenumbering{roman} % i, ii, iii...
  \pagestyle{fancy}
}
\newcommand{\mainmatter}{%
  \cleardoublepage
  \pagenumbering{arabic} % 1, 2, 3...
  \pagestyle{fancy}
}

% Cover page utility (no page number)
\newenvironment{coverpage}{\thispagestyle{empty}}{\clearpage}

% Center figures and tables by default
\AtBeginEnvironment{figure}{\centering}
\AtBeginEnvironment{table}{\centering}

% Caption font 11pt (you may change to 12pt if preferred)
\DeclareCaptionFont{elevenpt}{\fontsize{11}{13}\selectfont}
\captionsetup{font=elevenpt,labelfont=bf}

% TOC/LOF/LOT: titles 12pt bold, single-spacing inside lists
\renewcommand{\cfttoctitlefont}{\bfseries\fontsize{12}{18}\selectfont\MakeUppercase}
\renewcommand{\cftloftitlefont}{\bfseries\fontsize{12}{18}\selectfont\MakeUppercase}
\renewcommand{\cftlottitlefont}{\bfseries\fontsize{12}{18}\selectfont\MakeUppercase}
\setlength{\cftbeforetoctitleskip}{0pt}
\setlength{\cftaftertoctitleskip}{12pt}
\setlength{\cftbeforeloftitleskip}{0pt}
\setlength{\cftafterloftitleskip}{12pt}
\setlength{\cftbeforelottitleskip}{0pt}
\setlength{\cftafterlottitleskip}{12pt}
\let\OldTOC\tableofcontents
\renewcommand{\tableofcontents}{\begingroup\singlespacing\OldTOC\endgroup}
\let\OldLOF\listoffigures
\renewcommand{\listoffigures}{\begingroup\singlespacing\OldLOF\endgroup}
\let\OldLOT\listoftables
\renewcommand{\listoftables}{\begingroup\singlespacing\OldLOT\endgroup}

% Headings (Left-justified)
% HEADING 1: Chapter — 12pt, BOLD, UPPERCASE, before=0, after=12, LS=1.5
\titleformat{\chapter}[block]
  {\bfseries\fontsize{12}{18}\selectfont\setstretch{1.5}}
  {\thechapter}{1em}{\MakeUppercase}
\titlespacing*{\chapter}{0pt}{-20pt}{12pt}

% HEADING 2: Section — 12pt, BOLD, before=0, after=10, LS=1.5
\titleformat{\section}[block]
  {\bfseries\fontsize{12}{18}\selectfont\setstretch{1.5}}
  {\thesection}{1em}{}
\titlespacing*{\section}{0pt}{0pt}{10pt}

% HEADING 3: Subsection — 12pt, BOLD, before=0, after=8, LS=1.5
\titleformat{\subsection}[block]
  {\bfseries\fontsize{12}{18}\selectfont\setstretch{1.5}}
  {\thesubsection}{1em}{}
\titlespacing*{\subsection}{0pt}{0pt}{8pt}

% HEADING 4: Subsubsection — 12pt, BOLD, before=0, after=6, LS=1.5
\titleformat{\subsubsection}[block]
  {\bfseries\fontsize{12}{18}\selectfont\setstretch{1.5}}
  {\thesubsubsection}{1em}{}
\titlespacing*{\subsubsection}{0pt}{-10pt}{6pt}

% HEADING 5: Paragraph — 12pt, BOLD, before=0, after=6, LS=1.5
\titleformat{\paragraph}[block]
  {\fontsize{12}{18}\selectfont\setstretch{1.5}}
  {\theparagraph}{1em}{}
\titlespacing*{\paragraph}{0pt}{0pt}{18pt}

% Normal text environment with 18pt spacing after
\newenvironment{normaltext}{%
  \par
  \fontsize{12}{18}\selectfont
  \setstretch{1.5}%
  \setlength{\parskip}{18pt}%     % No automatic spacing
  \setlength{\parindent}{0pt}%   % No indent
  \setlength{\parskip}{0pt plus 0pt}% Reset
}{%
  \par
  \vspace{18pt}%                 % Add 18pt after environment ends
}

% Notes:
% - This class uses Times-like fonts via newtxtext/newtxmath (pdfLaTeX).
% - For exact "Times New Roman", compile with XeLaTeX and replace font setup:
%   \RequirePackage{fontspec}
%   \setmainfont{Times New Roman}
%   \setsansfont{Times New Roman}
%   \setmonofont{Times New Roman}
