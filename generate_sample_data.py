"""
Generate sample data for fake news detection
"""
import pandas as pd
import numpy as np
import random
import os

def generate_sample_data(n_samples=100, output_file="data/news_articles.csv"):
    """
    Generate a sample dataset of fake and real news
    
    Args:
        n_samples (int): Number of samples to generate
        output_file (str): Path to save the dataset
    """
    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Lists to store data
    titles = []
    texts = []
    labels = []
    
    # Real news templates
    real_titles = [
        "New Study Shows {topic} Benefits",
        "Researchers Discover {topic} Connection",
        "{location} Announces New {topic} Policy",
        "Scientists Make Progress on {topic} Research",
        "Report: {topic} Improvements in {location}",
        "{organization} Releases {topic} Statistics",
        "Experts Discuss {topic} Developments",
        "{person} Speaks About {topic} at Conference"
    ]
    
    real_text_templates = [
        "A new study published in the {journal} has found that {finding}. Researchers from {university} conducted the study over a period of {time_period}. The results suggest that {conclusion}. Dr. {person}, who led the research, said: '{quote}'. The study involved {number} participants and controlled for various factors including {factors}.",
        
        "Officials in {location} have announced a new policy regarding {topic}. The policy will take effect on {date} and aims to {goal}. '{quote}', said {person}, the {title} of {organization}. The announcement follows months of {activity} and consultation with {stakeholders}.",
        
        "A report released by {organization} shows {finding} related to {topic}. The data was collected from {sources} over {time_period}. According to the report, {conclusion}. Experts say this information will help {benefit}. The full report is available on the organization's website."
    ]
    
    # Fake news templates
    fake_titles = [
        "SHOCKING: {topic} Secret They Don't Want You To Know",
        "BREAKING: {person} Reveals Dangerous {topic} Cover-up",
        "What The Government Is Hiding About {topic}",
        "URGENT: {topic} Crisis That Media Won't Report",
        "The {topic} Conspiracy That Threatens {location}",
        "MIRACLE: {topic} Discovery Cures All Diseases",
        "WARNING: {topic} Danger Exposed By Whistleblower",
        "{person} Exposes TRUTH About {topic} Scandal"
    ]
    
    fake_text_templates = [
        "Anonymous sources have revealed shocking information about {topic} that the mainstream media refuses to report. According to these insiders, {false_claim}. This information has been deliberately suppressed because {conspiracy_reason}. The whistleblower, who wishes to remain anonymous for safety reasons, claims that '{false_quote}'. What they don't want you to know is that {exaggerated_claim}. Share this before it gets taken down!",
        
        "A groundbreaking discovery about {topic} is being hidden from the public. Scientists who have studied this phenomenon for years have found that {false_claim}. However, {organization} has been working to keep this information secret because {conspiracy_reason}. One expert, who was silenced by the authorities, managed to reveal that '{false_quote}'. The truth is that {exaggerated_claim}. This information is being censored everywhere!",
        
        "URGENT ALERT: A major crisis involving {topic} is unfolding, but the media is completely silent. Multiple sources confirm that {false_claim}. The government doesn't want you to panic, but {exaggerated_claim}. An insider from {organization} leaked that '{false_quote}'. This is happening right now and no one is talking about it! Wake up and share this message before it's too late!"
    ]
    
    # Content elements
    topics = ["Health", "Climate", "Education", "Technology", "Economy", "Energy", "Nutrition", "Security"]
    locations = ["New York", "California", "London", "Tokyo", "Berlin", "Sydney", "Paris", "Beijing"]
    organizations = ["WHO", "United Nations", "Harvard University", "Microsoft", "Google", "NASA", "CDC", "Oxford University"]
    persons = ["Dr. Smith", "Professor Johnson", "Dr. Williams", "Sarah Parker", "Michael Brown", "Dr. Garcia", "Emma Wilson", "Robert Miller"]
    journals = ["Nature", "Science", "The Lancet", "Journal of Medicine", "Environmental Science", "Educational Review"]
    universities = ["Harvard", "Stanford", "MIT", "Oxford", "Cambridge", "Yale", "Princeton", "Columbia"]
    time_periods = ["six months", "two years", "a decade", "five years", "18 months", "three years"]
    
    # Generate samples
    for i in range(n_samples):
        # Decide if this is real or fake news
        is_real = random.choice([True, False])
        
        if is_real:
            # Generate real news
            topic = random.choice(topics)
            location = random.choice(locations)
            organization = random.choice(organizations)
            person = random.choice(persons)
            
            # Generate title
            title_template = random.choice(real_titles)
            title = title_template.format(
                topic=topic,
                location=location,
                organization=organization,
                person=person
            )
            
            # Generate text
            text_template = random.choice(real_text_templates)
            text = text_template.format(
                topic=topic,
                location=location,
                organization=organization,
                person=person,
                journal=random.choice(journals),
                university=random.choice(universities),
                time_period=random.choice(time_periods),
                finding="significant improvements in " + topic.lower() + " outcomes",
                conclusion="further research is needed to fully understand the implications",
                quote="This is an important step forward in our understanding of " + topic.lower(),
                number=str(random.randint(100, 5000)),
                factors="age, gender, and socioeconomic status",
                date="January " + str(random.randint(1, 30)) + ", " + str(random.randint(2023, 2025)),
                goal="improve " + topic.lower() + " outcomes for all citizens",
                title="Director",
                activity="public debate",
                stakeholders="industry experts and community representatives",
                sources="multiple reliable sources",
                benefit="inform future policy decisions"
            )
            
            label = 1  # Real news
            
        else:
            # Generate fake news
            topic = random.choice(topics)
            location = random.choice(locations)
            organization = random.choice(organizations)
            person = random.choice(persons)
            
            # Generate title
            title_template = random.choice(fake_titles)
            title = title_template.format(
                topic=topic,
                location=location,
                organization=organization,
                person=person
            )
            
            # Generate text
            text_template = random.choice(fake_text_templates)
            text = text_template.format(
                topic=topic,
                false_claim=topic + " is actually a government experiment gone wrong",
                conspiracy_reason="it would expose powerful interests",
                false_quote="I've seen the documents proving that " + topic.lower() + " is not what people think it is",
                exaggerated_claim="this will affect 90% of the population within months",
                organization=organization
            )
            
            label = 0  # Fake news
        
        # Add to lists
        titles.append(title)
        texts.append(text)
        labels.append(label)
    
    # Create DataFrame
    df = pd.DataFrame({
        'title': titles,
        'text': texts,
        'label': labels
    })
    
    # Shuffle the data
    df = df.sample(frac=1).reset_index(drop=True)
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Generated {n_samples} samples and saved to {output_file}")
    print(f"Real news: {sum(labels)}, Fake news: {n_samples - sum(labels)}")

if __name__ == "__main__":
    generate_sample_data(200)