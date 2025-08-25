from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors

# Output path for redesigned version
output_path_modern = "Jo_Van_Montfort_CV_Modern.pdf"

doc = SimpleDocTemplate(output_path_modern, pagesize=A4,
                        rightMargin=20, leftMargin=20,
                        topMargin=20, bottomMargin=20)

# Define soft green/blue colors
left_bg_color = colors.HexColor("#E8F4F8")  # Very light blue
accent_color = colors.HexColor("#2E86AB")   # Soft blue
dark_text = colors.HexColor("#2E4053")      # Dark blue-gray

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="LeftSectionHeader", fontSize=12, leading=15, spaceAfter=6, textColor=accent_color))
styles.add(ParagraphStyle(name="LeftBodyText", fontSize=9.5, leading=12, textColor=dark_text))
styles.add(ParagraphStyle(name="HeaderName", fontSize=18, leading=22, textColor=dark_text, spaceAfter=6, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="SubHeader", fontSize=11, leading=14, textColor=accent_color, spaceAfter=6, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="RightSectionHeader", fontSize=13, leading=16, spaceAfter=8, textColor=accent_color, spaceBefore=12))
styles.add(ParagraphStyle(name="RightBodyText", fontSize=10, leading=13, textColor=colors.black))
styles.add(ParagraphStyle(name="Company", fontSize=11, leading=14, textColor=dark_text, spaceAfter=3))
styles.add(ParagraphStyle(name="JobTitle", fontSize=10, leading=13, textColor=accent_color, spaceAfter=3))
styles.add(ParagraphStyle(name="Date", fontSize=9, leading=11, textColor=colors.HexColor("#7F8C8D"), spaceAfter=6))

# Create a function to add background to the left column
def add_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(left_bg_color)
    canvas.rect(0, 0, 150, A4[1], fill=1, stroke=0)
    canvas.restoreState()

# Create elements list
elements = []

# First page with two-column layout
left_col = []
left_col.append(Paragraph("Jo Van Montfort", styles["HeaderName"]))
left_col.append(Paragraph("Software Architect", styles["SubHeader"]))
left_col.append(Spacer(1, 12))

left_col.append(Paragraph("<b>Contact</b>", styles["LeftSectionHeader"]))
left_col.append(Paragraph("📞 +32 483 666 349<br/>✉️ jovm007me@gmail.com", styles["LeftBodyText"]))
left_col.append(Paragraph("🔗 <a href='https://www.linkedin.com/in/jo-van-montfort-3264a588' color='#2E86AB'>LinkedIn</a>", styles["LeftBodyText"]))
left_col.append(Paragraph("💻 <a href='https://github.com/JoVanMontfort' color='#2E86AB'>GitHub</a>", styles["LeftBodyText"]))
left_col.append(Spacer(1, 12))

left_col.append(Paragraph("<b>Top Skills</b>", styles["LeftSectionHeader"]))
left_col.append(Paragraph("• Software Development<br/>• Java<br/>• Embedded Systems<br/>• AI/ML Solutions<br/>• Data Engineering", styles["LeftBodyText"]))
left_col.append(Spacer(1, 12))

left_col.append(Paragraph("<b>Languages</b>", styles["LeftSectionHeader"]))
left_col.append(Paragraph("Dutch (Native)<br/>English<br/>French<br/>Spanish (Elementary)", styles["LeftBodyText"]))
left_col.append(Spacer(1, 12))

left_col.append(Paragraph("<b>Certifications</b>", styles["LeftSectionHeader"]))
left_col.append(Paragraph("Oracle Certified Associate, Java SE 8 Programmer", styles["LeftBodyText"]))

# Right column content for first page
right_col = []
right_col.append(Spacer(1, 10))

right_col.append(Paragraph("<b>Summary</b>", styles["RightSectionHeader"]))
summary = """Started in 2007 as an embedded hardware/software developer in the automated guided vehicles industry. 
After a few years developing automated systems I realized my passion was solely software development. 
With more than 8 years of experience in Java, ORM, DDD, MVP and enterprise systems, I focus on building scalable, 
maintainable, and data-driven solutions. Passionate about turning data into actionable insights and delivering 
business value through technology."""
right_col.append(Paragraph(summary, styles["RightBodyText"]))
right_col.append(Spacer(1, 12))

right_col.append(Paragraph("<b>Experience</b>", styles["RightSectionHeader"]))

# TriggerIQ experience
triggeriq_details = """
<b>TriggerIQ — Founder</b><br/>
<i>June 2025 - Present (3 months) | Valencian Community, Spain</i><br/><br/>

• Lead product vision, growth strategy, and customer success for AI solutions company<br/>
• Defined company vision, product roadmap, and go-to-market strategy<br/>
• Built and led cross-functional teams across AI/ML, data engineering, and customer success<br/>
• Spearheaded development of core decision intelligence engine<br/>
• Secured strategic partnerships and early adopters<br/>
• Launched MVP in 2025, gaining early users within 8 weeks<br/>
• Reduced decision cycle time for clients using real-time insights
"""
right_col.append(Paragraph(triggeriq_details, styles["RightBodyText"]))
right_col.append(Spacer(1, 10))

# ReLeaseNow experience
releasenow_details = """
<b>ReLeaseNow.be — Founder</b><br/>
<i>June 2025 - Present (3 months) | Antwerp, Belgium</i><br/><br/>

• Founded Belgium's first digital platform for car lease transfers<br/>
• Defined and executed business model, product-market fit, and growth roadmap<br/>
• Led design of digital platform for lease matchmaking and contract transfer<br/>
• Integrated secure digital signature and ID verification tools<br/>
• Negotiated collaborations with leasing companies, automotive dealers, and legal advisors<br/>
• Created brand identity, messaging, and multi-channel ad strategy<br/>
• Ensured GDPR-compliant data flows and digital contract validity
"""
right_col.append(Paragraph(releasenow_details, styles["RightBodyText"]))
right_col.append(Spacer(1, 10))

# Two-column layout using a Table for first page
table_data = [[left_col, right_col]]
table = Table(table_data, colWidths=[150, 390])
table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 12),
    ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ("BACKGROUND", (0,0), (0,-1), left_bg_color),
]))

elements.append(table)
elements.append(PageBreak())

# Second page with right column alignment
# Create a table with an empty left column and content in the right column
empty_left_col = [Spacer(150, 10)]  # Empty spacer with same width as left column

# Right column content for second page
right_col_page2 = []
right_col_page2.append(Paragraph("<b>Experience (continued)</b>", styles["RightSectionHeader"]))
right_col_page2.append(Spacer(1, 12))

# CLdN experience
cldn_details = """
<b>CLdN ro-ro SA — JavaEE Software Engineer</b><br/>
<i>October 2019 - June 2025 (5 years 9 months) | Antwerp Area, Belgium</i><br/><br/>

• Designed and delivered highly available, low-latency applications for logistics processes<br/>
• Ensured ISO/TC 104 compliance with optimized architecture (Tomcat & Spring)<br/>
• Reduced time-to-market with optimized CI/CD pipeline (Jenkins, Wildfly, RedHat)<br/>
• Initiated transition to observability with ELK stack via Docker Compose<br/>
• Automated testing lifecycle with JUnit 5, Mockito, Cucumber, DbUnit<br/>
• Scrum team core contributor under SAFe methodology
"""
right_col_page2.append(Paragraph(cldn_details, styles["RightBodyText"]))
right_col_page2.append(Spacer(1, 10))

# Ravago experience (enhanced)
ravago_details = """
<b>Ravago — Freelance Java Developer</b><br/>
<i>October 2021 - December 2024 (3 years 3 months)</i><br/><br/>

• Designed and implemented scalable microservices architecture for chemical distribution systems<br/>
• Developed high-performance REST APIs handling complex chemical data and inventory management<br/>
• Optimized database performance through query optimization and indexing strategies<br/>
• Implemented CI/CD pipelines using Jenkins and Docker for automated deployment<br/>
• Enhanced system reliability through comprehensive testing with JUnit and Mockito<br/>
• Collaborated with cross-functional teams in an Agile/Scrum environment<br/>
• Integrated third-party APIs for logistics and supply chain management
"""
right_col_page2.append(Paragraph(ravago_details, styles["RightBodyText"]))
right_col_page2.append(Spacer(1, 10))

# Other experiences (condensed)
other_roles = """
<b>Danmo Solutions — Java Software Developer</b><br/>
<i>October 2021 - Present (3 years 11 months) | Schoten, Belgium</i><br/><br/>

<b>Vlaamse overheid — Java Software Engineer</b><br/>
<i>July 2019 - October 2019 (4 months) | Brussels Area, Belgium</i><br/><br/>

<b>Cheops Technology nv/sa — Java Software Engineer/Dev-Ops</b><br/>
<i>June 2019 - October 2019 (5 months) | Edegem</i><br/><br/>

<b>GET Time & Security Management Solutions — Software Designer Java</b><br/>
<i>September 2018 - June 2019 (10 months) | Antwerp Area, Belgium</i><br/><br/>

<b>Uitgeverij Van In — Software Designer Java</b><br/>
<i>May 2018 - September 2018 (5 months)</i>
"""
right_col_page2.append(Paragraph(other_roles, styles["RightBodyText"]))
right_col_page2.append(Spacer(1, 12))

right_col_page2.append(Paragraph("<b>Education</b>", styles["RightSectionHeader"]))
edu = """
<b>Hogeschool Dirksen</b> — HBO Bachelor, Embedded Engineering (2007 - 2009)<br/>
<b>KTA Schoten</b>
"""
right_col_page2.append(Paragraph(edu, styles["RightBodyText"]))

# Create a table for the second page with empty left column
table_data_page2 = [[empty_left_col, right_col_page2]]
table_page2 = Table(table_data_page2, colWidths=[150, 390])
table_page2.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 12),
    ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ("BACKGROUND", (0,0), (0,-1), left_bg_color),
]))

elements.append(table_page2)

doc.build(elements, onFirstPage=add_background, onLaterPages=add_background)

print(f"Modern CV created: {output_path_modern}")
