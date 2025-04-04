# Install moviepy if you haven't already:
# pip install moviepy
from moviepy import VideoFileClip, TextClip, concatenate_videoclips

# from moviepy.editor import TextClip, concatenate_videoclips

# Define video size and common properties
video_size = (1280, 720)
font = "Arial-Bold"  # Ensure you have this font or change accordingly
bg_color = "black"
text_color = "white"

# Create individual text clips for each scene
clip1 = TextClip("Escape the ordinary...",  color=text_color, bg_color=bg_color, size=video_size) \
    .set_duration(5)

clip2 = TextClip("From iconic landmarks to hidden gems,\nwe bring your dream destinations to life.", 
                 fontsize=40, color=text_color, bg_color=bg_color, size=video_size, method="caption") \
    .set_duration(10)

clip3 = TextClip("Whether you travel solo,\nwith family, or for romance,\nwe’ve got the perfect trip for you.", 
                 fontsize=40, color=text_color, bg_color=bg_color, size=video_size, method="caption") \
    .set_duration(10)

clip4 = TextClip("Seamless booking.\nPersonalized itineraries.\nLocal expertise.", 
                 fontsize=40, color=text_color, bg_color=bg_color, size=video_size, method="caption") \
    .set_duration(10)

clip5 = TextClip("Start your adventure today.\nVisit YourWebsite.com", 
                 fontsize=50, color=text_color, bg_color=bg_color, size=video_size, method="caption") \
    .set_duration(10)

# Concatenate all clips together
final_clip = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5])

# Export the final video
final_clip.write_videofile("travel_ad.mp4", fps=24)
