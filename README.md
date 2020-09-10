# SI 330 Fall 2020

## About this Course
*This is a programming course.*

This course offers more advanced material for BSI students that deepens knowledge of programming and software development beyond the 106/206 sequence, focusing especially on current computing methods and data structures for obtaining, transforming, and manipulating data. The skills covered in SI 330 will be critical for future Information Analytics and Data Science courses. This course is a programming course -- you will need to be a programmer to succeed.

Much of the work involved in data science (50-80% is the figure often quoted by data scientists, closer to 80-90% in my own professional experience) is not just in exploration or visualization, but in the initial data manipulation/engineering stages, e.g. gathering, transforming, cleaning, and aggregating. This is the "sewer work" of data science: it’s not glamorous but it’s absolutely critical. Thus, an important goal of the course is not only to cover specific Python-based tools for data manipulation, but also to teach useful high-level, step-by-step ways of thinking about and solving data computing problems, breaking down a complex task into the right kinds of intermediate stages. For example, the operations provided by many powerful data computing platforms, from SQL databases to Spark large-scale computing, can be thought of in terms of 'split-apply-combine' operations applied to data.  Given the fast-moving nature of data science and computing, you’ll find this high-level understanding very useful not only for using today’s computing tools, but for learning new technologies in the future.

## My Teaching Philosophy
I have two jobs in this course: (a) to teach you and help you learn and (b) to evaluate whether you have learned. Sometimes these roles conflict. I set a high bar on expectations, but my goal with the assessments I give is to lower the stakes at any one time, and give you ample opportunity to demonstrate to me that you are capable with this material. 

## Textbook & Technology
It is expected that you will have regular access to high speed consistent internet as well as a modern computing environment. The course will be offered **synchronously and it is expected that you will attend** all lectures and discussions and that attendance will be taken. A listing of course times is available on the [google calendar](https://calendar.google.com/calendar?cid=Y19qOWluMHJnbWtlODAxbzFhY2Y3bDVvZGhpb0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t) for the course.

We are not using Canvas! A goal of this course is to help you level up your git skills through repeated practice, so lecture materials and assignments will be posted to the [course github page](https://github.com/cab938/si330_fa20). Please create a github user account to receive weekly assignments. This is our programming environment: https://si330.mentoracademy.org/

The discussion forum for this course is in Google Rooms. You can find this in your UM gmail, or here: https://chat.google.com/room/AAAAo3Tpdy8

The principal textbook for the course is *Python for Data Analysis: Data Wrangling with Pandas, NumPy, and iPython* (2017) 2nd edition by Wes McKinney (O’Reilly).  The library has [digital copies](http://umich.summon.serialssolutions.com/2.0.0/link/0/eLvHCXMwpV09T8MwED2VhgEJqXwKyoe8sBFI7KSNJ4RoIgRIZYC5cuKLBCpR1SYD_x6fEwvowMKSxVLknBXfu7t37wCCtfvgvZnjwg-vmg89N48uhUblx1HsU8xLae0nfpvFD5lIe5C6vhiiWK5UaWJGApyrVjrCFVKt3ANlz9sxQddWu0mG0uDnWNyo5QZ4JPUe98GbTifp43fiRRrMQFPdN9t3_3An2QAcN6klkVi1JrfjNZ3Gf-9wBzykhoZd6GG1BwM3xoF1f_U-XDx_koAAM_CVTVStmBMquWS80izVltV1AK9Z-nJ373fTE_w3kmPww5Hx3OOgRBJcL3KJWsskipAXxH_iJgCVZZTkwiAQhVyUUogipKpZmeeK61AcwrYiln1V2248fQRsnOsoMdcALwRGOuHSgJ8YOZoYSKhEyWMYtuaYWXvMfn3y8K_FE9ji5DCJKxKcQr9eNngGnjX-eXeEX7lyrbw).

## Tentative Schedule of Topics
First 4-6 weeks: **Python Toolkits for Data Manipulation** (Python pandas)

|Date|Topics|
|-|-|
|September 1| Introduction, syllabus, overview of course, expectations, the Jupyter environment, python skills, introduction to regular expressions|
|September 3| Python skills assessment|
|September 8| [Regular expressions, Assignment 1 released](https://umich.zoom.us/rec/share/61uu3q-xTWFXhJNmXhMJswLS-Z-20BTgM8y9W8hY5VJsZRpdL6qvN5lzF-6R1IA0.goOAsukjtAA2Pn8M) |
|September 10| Numpy |
|September 15| Pandas, Assignment 2 released |



Next 4 weeks: **Scalable Structured Data** (SQL)

Next 4 weeks: **Big Data** (Apache Spark)

Last 2 weeks: **Extended Topics** (Data virtualization, SaaS computing paradigms, RPA)

## Grading
Grades are primarily based on individual assignments and these assignments are evenly weighted (10 assignments, 8% each = 80% of your grade). In addition, each week there will be a discussion section which you must attend, and each week the discussion section will have programming activities which are evenly weighted (10 discussion activities, 2% each = 20% of your grade). Late work is penalized at 10% per 24 hours late.

Tentative due dates and topics for the assignments are as follows (all due at **1:00 PM Ann Arbor time, right before class begins**). Assignments will be distributed through github at least one week in advance.

|Due Date | Topic|  Assignment Link|
|-|-|-|
|September 15th | Assignment 1, regular expressions| https://classroom.github.com/a/nhf1p7uI |
|September 22nd | Assignment 2, pandas| |
|September 29th | Assignment 3, pandas| |
|October 6th | Assignment 4, pandas| |
|October 13th | Assignment 5, pandas| |
|October 20th | Assignment 6, sql| |
|October 27th | Assignment 7, sql| |
|November 3rd | Assignment 8, sql| |
|November 10th | Assignment 9, spark| |
|November 17th | Assignment 10, spark| |

Assignments in this class are intended to be challenging and to demonstrate your skills with the materials! They are also commulative, in that you will require skills from earlier assignments (e.g. regular expressions) to complete later assignments (e.g. pandas data frame manipulation). In addition to these assignments, there is one optional **bonus opportunity worth up to 20%** which can be completed by the end of regular classes (December 8th). This assignment can be used to raise your grade or distinguish your abilities. The bonus assignment details will be released in mid-October.

Your letter grade will be assigned using the following formula:

|Total Scores | Letter Equivalent|
|-------------|------------------|
|>100         |A+                |
|95-100       |A                 |
|90-95        |A-                |
|85-90        |B+                |
|80-85        |B                 |
|75-80        |B-                |
|70-75        |C+                |
|65-70        |C                 |
|60-65        |C-                |
|55-60        |D+                |
|50-55        |D                 |
|<50          |E                 |

## UMSI specific policies

Please note the following UM or UMSI specific policies with respect to this course.

### COVID Statement
For the safety of all students, faculty, and staff on campus, it is important for each of us to be mindful of safety measures that have been put in place for our protection. By returning to campus, you have acknowledged your responsibility for protecting the collective health of our community.  Your participation in this course on an in-person basis is conditional upon your adherence to all safety measures mandated by the State of Michigan and the University, including maintaining physical distancing of six feet from others, and properly wearing a face covering in class.  Other applicable safety measures may be described in the [Wolverine Culture of Care](https://campusblueprint.umich.edu/uploads/Wolverine_Culture_of_Care%20sign_8.5x11_UPDATED_071520.pdf) and the [University’s Face Covering Policy for COVID-19](http://ehs.umich.edu/wp-content/uploads/2020/07/U-M-Face-Covering-Policy-for-COVID-19.pdf).  Your ability to participate in this course in-person as well as your grade may be impacted by failure to comply with campus safety measures.  Individuals seeking to request an accommodation related to the face covering requirement under the Americans with Disabilities Act should contact the [Office for Institutional Equity](https://oie.umich.edu/american-with-disabilities-act-ada/).  If you are unable or unwilling to adhere to these safety measures while in a face-to-face class setting, you will be required to participate on a remote basis (if available) or to disenroll from the class.  I also encourage you to review the [Statement of Students Rights and Responsibilities](https://oscr.umich.edu/statement), which includes a [COVID-related Statement Addendum](https://oscr.umich.edu/sites/oscr.umich.edu/files/2020_statement_addendum_final_approved.pdf).

### Student Mental Health and Wellbeing
The University of Michigan is committed to advancing the mental health and wellbeing of its students. If you or someone you know is feeling overwhelmed, depressed, and/or in need of support, services are available. For help, contact Counseling and Psychological Services (CAPS) at (734) 764-8312 and https://caps.umich.edu/ during and after hours, on weekends and holidays. You may also consult University Health Service (UHS) at (734) 764-8320 and https://www.uhs.umich.edu/mentalhealthsvcs, or for alcohol or drug concerns, see www.uhs.umich.edu/aodresources. Since many students are remote during fall 2020, [CAPS COVID-19 Support](https://caps.umich.edu/topic/caps-covid-19-support) features [SilverCloud](https://caps.umich.edu/silvercloud), an online, self-guided, interactive mental health resource that provides cognitive behavioral interventions.For a listing of other mental health resources available on and off campus, visit: http://umich.edu/~mhealth/

### Academic Integrity
Unless otherwise specified in an assignment all submitted work must be your own, original work. Any excerpts, statements, or phrases from the work of others must be clearly identified as a quotation, and a proper citation provided. Any violation of the School’s policy on Academic and Professional Integrity (stated in the Bachelor's, Master’s and Doctoral Student Handbooks) will result in serious penalties, which might range from failing an assignment, to failing a course, to being expelled from the program. Violations of academic and professional integrity will be reported to UMSI Student Affairs. Consequences impacting assignment or course grades are determined by the faculty instructor; additional sanctions may be imposed by the assistant dean for academic and student affairs.

### Accommodations for Students with Disabilities
If you think you need an accommodation for a disability, please let me know at your earliest convenience. Some aspects of this course, the assignments, the in-class activities, and the way we teach may be modified to facilitate your participation and progress. As soon as you make me aware of your needs, we can work with the Office of Services for Students with Disabilities (SSD) to help us determine appropriate accommodations. SSD (734-763-3000; http://ssd.umich.edu/) typically recommends accommodations through a Verified Individualized Services and Accommodations (VISA) form. I will treat any information that you provide in as confidential a manner as possible.
