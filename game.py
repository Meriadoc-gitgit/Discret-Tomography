from PIL import Image

from PIL import Image

def convert_to_binary(image_path, threshold=200):
  img = Image.open(image_path).convert('RGB')
  img = img.convert('L')  # Convert to grayscale

  # Apply threshold to convert to binary image
  binary_img = img.point(lambda p: 0 if p < threshold else 255)
  return binary_img

# Example usage:
image_path = 'cat.png'
binary_image = convert_to_binary(image_path)

# Save the binary image for visualization or further processing
binary_image.save('catbw.png')


def photo_to_nonogram_sequences(image_path):
  try:
    img = Image.open(image_path).convert('L')  # Convert image to grayscale
    width, height = img.size
    sequences = {
        'rows': [],
        'columns': []
    }

    # Generating sequences for rows
    for y in range(height):
      row_sequence = []
      consecutive_count = 0
      for x in range(width):
        pixel = img.getpixel((x, y))
        if pixel == 0:  # Assuming black represents filled cells
          consecutive_count += 1
        else:
          if consecutive_count > 0:
            row_sequence.append(consecutive_count)
            consecutive_count = 0
      if consecutive_count > 0:
        row_sequence.append(consecutive_count)
      sequences['rows'].append(row_sequence)

    # Generating sequences for columns
    for x in range(width):
      col_sequence = []
      consecutive_count = 0
      for y in range(height):
        pixel = img.getpixel((x, y))
        if pixel == 0:  # Assuming black represents filled cells
          consecutive_count += 1
        else:
          if consecutive_count > 0:
            col_sequence.append(consecutive_count)
            consecutive_count = 0
      if consecutive_count > 0:
        col_sequence.append(consecutive_count)
      sequences['columns'].append(col_sequence)

    return sequences

  except Exception as e:
    print("Error processing the image:", e)
    return None
