def get_career_roadmap(career_field):
    """Tool to get career roadmap and skills needed for a chosen field"""
    
    # Career roadmap database
    roadmaps = {
        'software developer': {
            'skills': ['Programming Languages (Python, JavaScript)', 'Data Structures & Algorithms', 'Version Control (Git)', 'Databases', 'Web Development'],
            'timeline': '6-12 months',
            'difficulty': 'Medium',
            'resources': ['FreeCodeCamp', 'LeetCode', 'GitHub', 'Stack Overflow']
        },
        'data scientist': {
            'skills': ['Python/R', 'Statistics', 'Machine Learning', 'SQL', 'Data Visualization'],
            'timeline': '8-15 months',
            'difficulty': 'Hard',
            'resources': ['Kaggle', 'Coursera', 'Jupyter Notebooks', 'Pandas Documentation']
        },
        'digital marketing': {
            'skills': ['SEO/SEM', 'Social Media Marketing', 'Content Creation', 'Analytics', 'Email Marketing'],
            'timeline': '3-6 months',
            'difficulty': 'Easy-Medium',
            'resources': ['Google Analytics Academy', 'HubSpot Academy', 'Facebook Blueprint']
        },
        'product manager': {
            'skills': ['Product Strategy', 'User Research', 'Data Analysis', 'Communication', 'Agile/Scrum'],
            'timeline': '6-10 months',
            'difficulty': 'Medium-Hard',
            'resources': ['Product School', 'Coursera PM Courses', 'Medium Articles']
        },
        'cybersecurity': {
            'skills': ['Network Security', 'Ethical Hacking', 'Risk Assessment', 'Compliance', 'Incident Response'],
            'timeline': '8-12 months',
            'difficulty': 'Hard',
            'resources': ['CompTIA Security+', 'Cybrary', 'SANS Training']
        }
    }
    
    # Find matching career field
    career_lower = career_field.lower()
    for key, roadmap in roadmaps.items():
        if key in career_lower or any(word in career_lower for word in key.split()):
            return roadmap
    
    # Default roadmap for unknown fields
    return {
        'skills': ['Research the field', 'Network with professionals', 'Gain relevant experience', 'Develop core competencies'],
        'timeline': '6-12 months',
        'difficulty': 'Medium',
        'resources': ['LinkedIn Learning', 'Industry blogs', 'Professional associations', 'Online courses']
    }
