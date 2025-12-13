"""
Convert CV text file to professional PDF
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.colors import HexColor
from datetime import datetime

def create_cv_pdf():
    """Convert CV text to PDF with professional formatting"""
    
    # Read the CV text file
    with open('Serghei_Covalciuc_CV.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create PDF
    filename = f"Serghei_Covalciuc_CV_{datetime.now().strftime('%Y%m%d')}.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Define custom styles
    styles = getSampleStyleSheet()
    
    # Header style (Name)
    name_style = ParagraphStyle(
        'CustomName',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#1e3a8a'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Subtitle style (Title)
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#0ea5e9'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # Contact info style
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # Section header style
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=HexColor('#1e3a8a'),
        spaceAfter=10,
        spaceBefore=16,
        fontName='Helvetica-Bold',
        borderWidth=1,
        borderColor=HexColor('#0ea5e9'),
        borderPadding=5,
        backColor=HexColor('#f0f9ff')
    )
    
    # Body text style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8,
        alignment=TA_JUSTIFY,
        fontName='Helvetica',
        leading=14
    )
    
    # Bullet point style
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=10,
        leftIndent=20,
        spaceAfter=6,
        fontName='Helvetica',
        leading=13
    )
    
    # Build PDF content
    story = []
    
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Skip separator lines
        if '=' * 10 in line or not line:
            continue
        
        # Name (first line)
        if line == "SERGHEI COVALCIUC":
            story.append(Paragraph(line, name_style))
            
        # Subtitle
        elif "Data Analytics Enthusiast" in line:
            story.append(Paragraph(line, subtitle_style))
            
        # Contact info
        elif any(x in line for x in ['Email:', 'Phone:', 'LinkedIn:', 'GitHub:', 'Portfolio:']):
            # Remove labels and create clickable links
            if 'Email:' in line:
                email = line.split('Email:')[1].strip()
                story.append(Paragraph(f'<a href="mailto:{email}">{email}</a>', contact_style))
            elif 'Phone:' in line:
                story.append(Paragraph(line.replace('Phone:', '📱'), contact_style))
            elif 'LinkedIn:' in line:
                url = line.split('LinkedIn:')[1].strip()
                story.append(Paragraph(f'<a href="https://{url}" color="blue">LinkedIn: {url}</a>', contact_style))
            elif 'GitHub:' in line:
                url = line.split('GitHub:')[1].strip()
                story.append(Paragraph(f'<a href="https://{url}" color="blue">GitHub: {url}</a>', contact_style))
            elif 'Portfolio:' in line:
                url = line.split('Portfolio:')[1].strip()
                story.append(Paragraph(f'<a href="https://{url}" color="blue">Portfolio: {url}</a>', contact_style))
        
        # Section headers
        elif line.isupper() and len(line) > 5 and 'SERGHEI' not in line:
            story.append(Spacer(1, 0.15*inch))
            story.append(Paragraph(line, section_style))
            
        # Bullet points
        elif line.startswith('•'):
            text = line.replace('•', '•', 1)
            story.append(Paragraph(text, bullet_style))
            
        # Job/Project titles (lines that don't start with bullet but have pipe separator)
        elif '|' in line and not line.startswith('•'):
            parts = line.split('|')
            if len(parts) == 2:
                title_style = ParagraphStyle(
                    'JobTitle',
                    parent=styles['Normal'],
                    fontSize=11,
                    fontName='Helvetica-Bold',
                    spaceAfter=4,
                    spaceBefore=8,
                    textColor=HexColor('#334155')
                )
                story.append(Paragraph(f"<b>{parts[0].strip()}</b> | <i>{parts[1].strip()}</i>", title_style))
            else:
                story.append(Paragraph(line, body_style))
        
        # Regular paragraphs
        elif line:
            story.append(Paragraph(line, body_style))
    
    # Build PDF
    doc.build(story)
    print(f"✅ CV saved to: {filename}")
    return filename

if __name__ == "__main__":
    try:
        pdf_file = create_cv_pdf()
        print(f"\n📄 Your CV has been converted to PDF!")
        print(f"📁 Location: {pdf_file}")
        print(f"\n💡 You can now:")
        print(f"   • Email this PDF to employers")
        print(f"   • Upload to job applications")
        print(f"   • Print for in-person interviews")
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"\nTrying to install required package...")
        import subprocess
        subprocess.run(['pip', 'install', 'reportlab'])
        print(f"\nPlease run the script again!")
