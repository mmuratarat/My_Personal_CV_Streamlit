from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
favicon_pic = current_dir / "assets" / "favicon.ico"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Mustafa Murat ARAT"
im = Image.open(favicon_pic)
NAME = "Mustafa Murat ARAT"
DESCRIPTION = """
Statistician | Data Scientist | Machine Learning (Deep Learning) Specialist
"""
WEBPAGE = "https://mmuratarat.github.io "
EMAIL = "arat.murat@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/mmuratarat"
GITHUB = "https://github.com/mmuratarat"


st.set_page_config(page_title=PAGE_TITLE, page_icon=im, layout="wide")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=350)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📌", WEBPAGE)
    st.write("📌", EMAIL)
    st.write("📌", LINKEDIN)
    st.write("📌", GITHUB)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("PROFESSIONAL SUMMARY")
st.write(
    """
- ✔️ PhD-level educated, bilingual statistician and data scientist, who works to design, develop and implement advanced data-driven predictive methods, powered by machine learning and deep learning algorithms, to provide actionable insights from large volumes of real-world, structured and unstructured data in order to satisfy the business needs / goals for decision making across different industries and roles. I have a deep understanding of best data analytic practices to solve complex problems and I continuously improve myself and learn new emerging technologies, tools, and platforms to add new skills to my skill set.
- ✔️ I believe that I have a team-oriented, can-do attitude, strong enthusiasm and a deep curiosity about the intersection of business and technology. I am passionate, highly motivated, innovative, energetic, reliable, inclusive and pro-diversity, and have excellent written and verbal communication skills.
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("SKILLS")
st.write(
    """
- **Programming Languages/Libraries**: Python, Numpy, Pandas, scikit-learn, statsmodels, psycopg2, spaCy, NLTK, OpenCV and matplotlib, seaborn, plotly etc...
- **Deep Learning Libraries**: Tensorflow, and Keras.
- **Container and Orchestration Systems**: Docker, Swarm, Kubernetes.
- **Database Systems**: PostgreSQL (with pgadmin4 or DataGrip)
- **No-SQL/Full-text Search Systems**: MongoDB and Elasticsearch/Kibana
- **Big Data Frameworks**: Apache Spark
- **Scripting Languages**: R, and MATLAB.
- **Visualization Software**: Tableau.
- **Statistical Softwares**: SPSS, and Minitab
- **Version Control**: Git/Github
- **Markup Languages**: HTML, LATEX, Beamer, Jekyll, and Markdown/R-Markdown.
- **Miscellaneous**: Extensive usage of JupyterLab (notebooks) and comfortable with Bash command line interface.
- **Languages**: Turkish (Native Language), English (Full professional proficiency), French (Elementary proficiency)
"""
)

# --- HONORS, AWARDS AND SCHOLARSHIPS ---
st.write("#")
st.subheader("HONORS, AWARDS AND SCHOLARSHIPS")
st.write("---")
st.write(
    """
    - ► Secured Supreme Success Award from Faculty of Science of Hacettepe University for the semester 2009–2010.
    - ► Recipient of Scholarship/Assistantship from Department of Business Analytics & Statistics of Tennessee, Knoxville for my doctoral studies between the years 2015 – 2020.
    - ► Earned Statistics Excellence Fund from Department of Business Analytics & Statistics of Tennessee, Knoxville for the Fall semester of 2015.
    """
    )


# --- PROJECTS AND TRAININGS ---
st.write("#")
st.subheader("PROJECTS AND TRAININGS")
st.write("---")

# --- PROJECT 1
st.write("✪", "***Sales Elasticity of Emotional Displays***")
st.write("2019 - 2020")
st.write(
    """
- ► This project was part of one of my chapters of my doctoral thesis through an American direct-to-consumer retailer company.
- ► It marks the first empirical approach which establishes the sales elasticity of emotional displays in sales pitches.
- ► We apply state-of-the art artificial intelligence technology to almost two years of video footage (17,312 hours or 62.32 million frames), in which a TV host makes her/his sales pitch to customers, to detect human faces and Salesperson’s facial emotions are then extracted and classified into six emotional displays: happiness, sadness, surprise, anger, fear, and disgust. We, then, matched them to customers' purchase data to understand the true nature of the relationship. To estimate sales elasticity, we incorporate emotional displays in sales response models together with marketing mix activities (i.e., product, price, display duration, and free shipping).
- ► We found that the sales elasticities of a host's emotional displays are uniformly negative, including that of happiness, which is a provocative finding (against “service with a smile” policy) because it partially contradicts the external validity of social contagion theory. In other words, emotional displays in sales pitches are hazardous to business, salespersons should pitch with neutral expressions (i.e., absence of emotion). Additionally, we found that the presence (versus absence) of a host’s face in the frame positively increases sales by 0.62%. Therefore, the study offers guidance to firms on re-training low performers on “selling with a straight face” as well as to reward successful hosts
- ► It was published in Journal of Marketing in February, 2022.
"""
)

# --- PROJECT 2
st.write("✪", "***Working Group on the Development of Health Policies | Ministry of Health of the Republic of Turkey***")
st.write("June 2022 - Present")
st.write(
    """
- ► Member.
- ► Having access to Turkish healthcare data of all the population, working on various scientific research activities to be carried out in all branches of medicine and conducting statistical and biostatistical methodologies and guiding research.
- ► www.saglik.gov.tr.
"""
)

# --- PROJECT 3
st.write("✪", "***Intervention 10: Research on Occupational Accident Prediction Model***")
st.write("July 2022 - Present")
st.write(
    """
- ► Consultant / Senior Non-Key Expert.
- ► Part of the European Union Project “Technical Assistance for Strengthening Training and Research Capacity of the Centre for Labour and Social Training and Research (ÇASGEM)” (TREESP1.3.CASGEM/P-01, EuropeAid/140073/IH/SER/TR).
- ► by Directorate of European Union and Finance Assistance (DEUFA) in the Ministry of Labour and Social Security of the Republic of Turkey.
- ► Having access to Turkish occupational accident database maintained by the Social Security Institution of Republic of Turkey, my responsibilities are:  
(1) To find out the most relevant and important variables affecting to the causes of occupational accidents.
(2) To use statistical methods for the selection of the most significant variables and excluding the non-significant variables from the available data set for the design of the accident prediction models.
(3) To experiment different statistical models and/or algorithms using Python programming language in order to find best predictions models for construction (building), mining (coalmine), chemical (petrochemical) and metal (moulding) since they account for more than 44.7% of all occupational accidents.
(4) To design an evidence-based modelling on occupational accidents for assisting the OHS legislation and reducing the number of occupational accidents in the project’s four industrial sectors.
(5) To write the final report and sharing the work of the research study group with other governmental organizations, project’s stakeholder groups as well as the broader public audience.
(6) To support on how to use the selected models/algorithms accidents in the project’s four industrial sectors.
- ► www.casgemeuproject.org
"""
)

# --- PROJECT 4
st.write("✪", "***Intervention 5.5.: Training on Advanced Statistical Analysis Method for Health Physical and Social Sciences in Occupational Health and Safety***")
st.write("March 2022 - June 2022")
st.write(
    """
- ► Trainer / Senior Non-Key Expert.
- ► Part of the European Union Project “Technical Assistance for Strengthening Training and Research Capacity of the Centre for Labour and Social Training and Research (ÇASGEM)” (TREESP1.3.CASGEM/P-01, EuropeAid/140073/IH/SER/TR).
- ► by Directorate of European Union and Finance Assistance (DEUFA) in the Ministry of Labour and Social Security of the Republic of Turkey.
- ► for 1st, 2nd and 3rd Sessions.
- ► Total 75 participants.
- ► Covering multiple topics including but are not limited to analysis of variance (ANOVA) and analysis of variance (ANCOVA), linear regression, logistic regression, regularization techniques, generalized linear models, dimension reduction techniques, non-parametric methods, imbalanced learning and performing all these techniques using real-world datasets by using Python programming language and its libraries.
- ► www.casgemeuproject.org
"""
)

# --- PROJECT 5
st.write("✪", "***Intervention 5.4.: Training on Basic Statistical Analysis Method for Health Physical and Social Sciences in Occupational Health and Safety***")
st.write("August 2021 - December 2021")
st.write(
    """
- ► Trainer / Senior Non-Key Expert.
- ► Part of the European Union Project “Technical Assistance for Strengthening Training and Research Capacity of the Centre for Labour and Social Training and Research (ÇASGEM)” (TREESP1.3.CASGEM/P-01, EuropeAid/140073/IH/SER/TR).
- ► by Directorate of European Union and Finance Assistance (DEUFA) in the Ministry of Labour and Social Security of the Republic of Turkey.
- ► for 2nd and 3rd Sessions.
- ► Total 50 participants.
- ► Covering multiple topics including but are not limited to measures of location and dispersion and their appropriate uses, random variables, discrete/continuous probability distributions, hypothesis testing, confidence intervals, Chi-square and tests of contingency tables, simple linear regression and one-way analysis of variance (ANOVA) and applying everything by using Python programming language and its libraries.
- ► www.casgemeuproject.org
"""
)

# --- PROJECT 6
st.write("✪", "***Training for “Machine Learning” | Presidency of Turkey, Presidency of Strategy and Budget***")
st.write("March 7, 2022 - April 1, 2022")
st.write(
    """
- ► Trainer.
- ► Hybrid Model (Online Class + Face-to-Face), Around 35 participants.
- ► Covering multiple topics including but are not limited to data engineering (scaling the data, missing value imputation, outlier detection, encoding categorical variables, feature selection, hyperparameter tunning, model evaluation criteria etc.), classification, clustering and regression methods (linear regression, logistic regression, regularization, k-nearest neighbors algorithm, support vector machines, decision trees, ensemble learning, k-means etc.), dimensionality reduction methods (factor analysis and principal component analysis) and performing these techniques using real-world datasets by using Python programming
- ► www.sbb.gov.tr
"""
)

# --- PROJECT 7
st.write("✪", "***Training for “Data Analysis with Python” | Presidency of Turkey, Presidency of Strategy and Budget***")
st.write("January 24, 2022 - February 7, 20222")
st.write(
    """
- ► Trainer.
- ► Hybrid Model (Online Class + Face-to-Face), Around 35 participants
- ► Covering multiple topics including but are not limited to primitive and non-primitive data structures in Python, control-flow, object-oriented programming, NumPy and pandas libraries, string manipulation, data visualization etc.
- ► www.sbb.gov.tr
"""
)

# --- PROJECT 8
st.write("✪", "***Online training for “Artificial Intelligence”***")
st.write("March 26, 2022 - April 17, 2022")
st.write(
    """
- ► Trainer.
- ► 4 weeks online training from zero to expertise, www.yapayzeka.us
- ► About 70 participants.
- ► Covering multiple topics Python, Statistics, Machine Learning / Deep Learning algorithms.
"""
)

# --- EDITOR AND TRANSLATOR ---
st.write("#")
st.subheader("EDITOR AND TRANSLATOR")
st.write("---")
st.write(
    """
    - ► Editor of the Turkish translation of the book “Automate the Boring Stuff with Python: Practical Programming for Total Beginners” by Al Sweigart, August 2022, Buzdağı Yayınevi, http://buzdagiyayinevi.com/python-ile-sikici-isleri-aninda-bitir-yeni-baslayanlar-icin-uygulamali-programlama/.
    - ► Editor of the Turkish translation of the book “Python Crash Course: A Hands-On, Project-Based Introduction to Programming” by Eric Matthes, March 2022, Buzdağı Yayınevi, http://buzdagiyayinevi.com/kapsamli-python-kursu-programlamaya-uygulamali-ve-proje-tabanli-giris/.
    - ► Editor of the Turkish translation of the book “Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems” by Aurelien Geron, 2021, Buzdağı Yayınevi, http://buzdagiyayinevi.com/scikit-learn-keras-ve-tensorflow-ile-uygulamali-makine-ogrenmesi/.
    - ► One of the translators of the Turkish translation of the book “Schaum’s Outline of Probability (2nd edition)” by Marc Lipson and Seymour Lipschutz, 2013, Nobel Yayın Dağıtım, https://www.nobelyayin.com/kitap_3893.html.
    - ► One of the translators of the Turkish translation of the book “Introduction to Probability” by George G Roussas, 2014, Nobel Yayın Dağıtım, https://www.nobelyayin.com/kitap_4207.html.
    """
    )

# --- INVITED TALKS / SEMINARS   ---
st.write("#")
st.subheader("INVITED TALKS / SEMINARS")
st.write("---")
st.write(
    """
    - ► Bringing Business, Statistical Methods and Transfer Learning Together: Sales Elasticity of Emotional Displays – Large Scale Evidence for Selling with a Straight Face, Department of Statistics, of Hacettepe University, December 29th 2020.
    - ► A New Livestream Retail Analytics Framework to Assess the Sales Impact of Emotional Display, Department of Statistics, of Middle East Technical University, May 27th 2021.
    - ► Introduction to Machine Learning and Basic Machine Learning Applications, Workshop for “Technical Assistance for Improving the Detection Capacity of Turkish Customs Enforcement” European Union Project, Abant, Bolu, Turkey, November 12nd 2021.
    - ► Intern Career Talk, Department of Computer Science, Manisa Celal Bayar University, April 4th 2022.
    """
    )

# --- EDUCATION ---
st.write("#")
st.subheader("EDUCATION")
st.write("---")

# ---  PHD
st.write("✪", "**Doctor of Philosophy in Analytics** | August 2015 – May 2020")
st.write("Department of Business Analytics & Statistics, University of Tennessee, Knoxville, U.S.A.")
st.write(
    """
- ► GPA: 3.92 / 4.00
- ► Coursework includes: Prescriptive Analytics, Statistical Inference, Probability/Stochastic Process, Bayesian Modeling and Computations, Data Mining Methods and Business Applications, Applied Multivariate Methods, Image Reconstruction, Reinforcement Learning, Applied Time Series, Probability and Mathematical Statistics, Multivariate Data Mining Techniques.
- ► Completed my dissertation “Advances and Applications in Deep Learning” under the supervision of Dr. Michel BALLINGS (mb@utk.edu), working on real-world structured/unstructured data through an American direct-to-consumer retailer.
"""
)

# --- MSC
st.write("✪", "**Master of Science in Statistics** | August 2011 – June 2014")
st.write("Department of Statistics, Hacettepe University, Ankara, Turkey")
st.write(
    """
- ► GPA: 3.93 / 4.00 (ranked 1st of 15)
- ► Coursework includes: Linear Models, Time Series, Stochastic Processes, The Analysis of Contingency Tables, Simulation Techniques, Multivariate Statistical Methods, Survival Analysis.
- ► Completed my master thesis titled “A Study on Support Vector Machines” under supervision of Prof. Dr. Turhan MENTES (mentes@hacettepe.edu.tr).
"""
)

# --- BSC
st.write("✪", "**Bachelor of Science in Statistics** | September 2007 – June 2011")
st.write("Department of Statistics, Hacettepe University, Ankara, Turkey")
st.write(
    """
- ► GPA: 3.24 / 4.00 (top 10%, ranked 9th of 91)
- ► Coursework includes: Categorical Data Analysis, Biostatistics, Econometrics, Time Series, Experimental Design, Multivariate Statistical Methods, Stochastic Processes, Sampling, Survey Design, Operation Research, Actuary, Regression Analysis, Probability, Mathematical Statistics, Nonparametric Statistical Methods, Statistical Decision Making, Linear Algebra, Calculus, (Advanced) Mathematics.
"""
)

# --- PROFESSIONAL EXPERIENCES ---
st.write("#")
st.subheader("PROFESSIONAL EXPERIENCES")
st.write("---")

# --- Research Assistant
st.write("✪", "**Research Assistant** | October 2011 – present")
st.write("Department of Statistics, Hacettepe University, Ankara, Turkey")
st.write(
    """
- ► Teaching a wide range of undergraduate-level courses from Bayesian Statistics to Probability Theory.
- ► Academic consultant for undergraduate students.
"""
)

# --- Research Assistant
st.write("✪", "**Graduate Teaching Assistant** | August 2015 – July 2020")
st.write("Department of Business Analytics & Statistics, University of Tennessee, Knoxville, U.S.A.")
st.write(
    """
- ► Assisting students during the lab sessions and marking written reports of the assignments for courses such as Categorical Data Analysis, Customer Analytics, Applied Multivariate Methods, Applied Time series and many more.
- ► Co-creating a Deep Learning class for the first time in the faculty with my advisor Dr. Michel Ballings, covering a wide range of topics, from Backpropagation to Convolutional Neural Networks, from Long Short-term Memory to Autoencoders.
"""
)
                                                                                                             
# --- PEER-REVIEWED PUBLICATIONS ---
st.write("#")
st.subheader("PEER-REVIEWED PUBLICATIONS")
st.write("---")
st.write(
    """
    - ► Tan, O., Hizli Sayar, GH., Ünsalver, B.Ö., **Arat, M. M.** and Karamustafalioglu, O. (2014). “The correlations of nicotine addiction with the levels of impulsiveness, depression and anxiety in obsessive-compulsive patients”. Journal of Dependence, 15(3), 124 - 133.
    - ► Gogcegoz Gül, I., Eryilmaz, G., Hizli Sayar, G., Özten, E., **Arat, M.M.**, and Tarhan, N. (2014). “Evaluation of the Efficacy of The Continuation Electroconvulsive Therapy in Treatment-Resistant Schizophrenia”. Revista de Psiquiatria Clínica, 41(4), 90 - 94
    - ► Eryilmaz, G. Gogcegoz Gül, I., Yorbik, O., and **Arat, M.M.** (2014). “Evaluation of Clinical Response According to Plasma Paroxetine Level in Paroxetine-Responsive Major Depression”. International Journal of Internal Medicine, 3(3), 39 - 42.
    - ► Tan, O., Hizli Sayar, G., Ünsalver, B.Ö., **Arat, M. M.** and Karamustafalioglu, O. (2015). “Combining transcranial magnetic stimulation and cognitive-behavioral therapy in treatment resistant obsessive-compulsive disorder”. Anatolian Journal of Psychiatry, 16(3), 180 - 188.
    - ► **Arat, M.M.**, Aktas, S. (2016). “Generalized Maximum Entropy Approach to Unreplicated Factorial Experiments”. Statistics and Its Interface, 9(3), 295 - 302.
    - ► Bharadwaj, N., Ballings, M., Naik, P., Moore, G.M., **Arat, M.M.** (2022). “A New Livestream Retail Analytics Framework to Assess the Sales Impact of Emotional Displays”. Journal of Marketing, 86(1), 27 – 47.
    - ► **Arat, M.M.** (2022). “Learning From High-Cardinality Categorical Features in Deep Neural Networks”. Journal of Advanced Research in Natural and Applied Sciences, 8 (2), 222 – 236.
    """
    )

# --- ORAL PRESENTATIONS ---
st.write("#")
st.subheader("ORAL PRESENTATIONS")
st.write("---")
st.write(
    """
    - ► **Mustafa Murat Arat**, “Testing Export-Led Growth Hypothesis: The Case of Turkey, 1961-2010”, Applied Statistics 2012, Ribno, Slovenia, September 23 – 26, 2012.
    - ► Elcin Ergin, **Mustafa Murat Arat**, Cem Iyigun, Inci Batmaz, “Short-Term Electricity Load Forecasting Via Nonparametric Prediction Methods”, EURO-INFORMS Joint International Meeting: 26th European Conference on Operational Research, Rome, Italy, July 1 - 4, 2013.
    - ► **Mustafa Murat Arat**, Elcin Ergin, “Short Term Load Forecasting Using Support Vector Regression”, European Conference on Data Analysis by The German Classification Society (GfKl) and the French speaking Classification Society (SFC), Luxembourg City, Luxembourg, July 1 – 4, 2013.
    - ► **Mustafa Murat Arat**, Serpil Aktas Altunay, "Generalized Maximum Entropy Approach To Unreplicated Factorial Experiments", The 13th Annual Conference of the European Network for Business and Industrial Statistics (ENBIS-13), September 15 – 19, 2013.
    - ► **Mustafa Murat Arat**, “Comparison of SVM and LS-SVM For Regression”, y-BIS 2013: Joint Meeting of Young Business and Industrial Statisticians, sponsored by International Society for Business and Industrial Statistics (ISBIS) and European Network for Business and Industrial Statistics (ENBIS), Istanbul, Turkey, September 19 – 21, 2013
    - ► Michel Ballings, Neeraj Bharadwaj, Prasad Naik, George Miller Moore, **Mustafa Murat Arat**, “But Wait, There’s More! Deep Learning of Sales Elasticity of Sales Pitches”, Theory + Practice in Marketing Conference, Columbia University, New York, NY, USA, May 18, 2019.
    - ► **Mustafa Murat Arat**, George Miller Moore, Michel Ballings, "Maximizing Insights from Customer Data Streams", Interactive Marketing Research Conference, Houston, TX, USA, March 27 – 29, 2019.
    - ► **Mustafa Murat Arat**, Michel Ballings, George Miller Moore, “Breaking Through Barriers to Deep Learning Adoption in Customer Behavior Modeling”, INFORMS Annual Meeting 2019, Seattle, WA, USA, October 20 - 23, 2019.
    - ► Neeraj Bharadwaj, Michel Ballings, Prasad Naik, Miller Moore, **Mustafa Murat Arat**, “Purchase Impact Of A Salesperson’s Facial Expressions: Large-Scale Video Analysis Using Deep Learning", 2020 Winter AMA Academic Conference, San Diego, CA, USA, February 14 - 16, 2020.
    - ► Osman Tolga Kaskati, **Mustafa Murat Arat**, Fatma Kaymakamtorunlari Deni̇z, Emre Keski̇n, “Popülasyon Genetiği Çalışmalarında Mantel Testi Üzerinde Bir Uygulama”, 22nd Local and 5th International Biostatistics Conference, Online, October 28 - 30, 2021.
    """
    )

# --- SCIENTIFIC ACTIVITIES   ---
st.write("#")
st.subheader("SCIENTIFIC ACTIVITIES")
st.write("---")
st.write(
    """
    - ► GIS 2013: Genç İstatistikçiler Sempozyumu (Young Statisticians Symposium), Member of the Local Organizing Committee, Ankara (Turkey), September 10 -11 2013, http://www.gis2013.hacettepe.edu.tr. 
    - ► AIK 2013: Araştırmacılar ve İstatistikçiler Konferansı (Researchers and Statisticians Conference), Member of the Local Organizing Committee, Ankara (Turkey), September 10 -11 2013, http://www.aik2013.hacettepe.edu.tr.
    - ► y-BIS 2013: Joint Meeting of Young Business and Industrial Statisticians, sponsored by ENBIS (European Network for Business and Industrial Statistics) and ISBIS (International Society for Business and Industrial Statistics), Member of the International Scientific Committee and Organizing Committee, Istanbul (Turkey), September 19 – 21, 2013, http://ybis13.msgsu.edu.tr.
    - ► y-BIS 2019: Joint Meeting of Young Business and Industrial Statisticians, sponsored by ENBIS (European Network for Business and Industrial Statistics) and ISBIS (International Society for Business and Industrial Statistics), Member of the International Scientific Committee and Organizing Committee, Istanbul (Turkey), September 25 – 28, 2019, http://ybis2019.msgsu.edu.tr.
    """
    )


# --- COLLOQUIUMS/MEETINGS/CONFERENCES ATTENDEE  ---
st.write("#")
st.subheader("COLLOQUIUMS/MEETINGS/CONFERENCES ATTENDEE")
st.write("---")
st.write(
    """
    - ► 8th International Statistics Students Colloquium, Izmir, Turkey, May 14 - 15, 2011.
    - ► The Joint Meeting of Young Business and Industrial Statisticians and Young Portuguese Statisticians, Lisbon, Portugal, July 23 - 26, 2012.
    - ► 9th International Statistics Days Symposium, Antalya, Turkey, May 10 - 14, 2014.
    """
    )


