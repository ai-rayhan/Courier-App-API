from django.core.exceptions import ValidationError
from PIL import Image

def validate_image(image):
    # Open the image using PIL
    img = Image.open(image)
    width, height = img.size
    
    # Ensure image has a 1:1 aspect ratio
    if width != height:
        raise ValidationError("Image must have a 1:1 aspect ratio.")
    
    # Check if image size is within 1 MB
    max_size_mb = 1
    max_size_bytes = max_size_mb * 1024 * 1024  # Convert MB to bytes
    if image.size > max_size_bytes:
        raise ValidationError(f"Image size must be less than {max_size_mb} MB.")