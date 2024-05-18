import cv2
import pytesseract

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Remove noise from the thresholded image
    denoised_image = cv2.fastNlMeansDenoising(binary_image, None, 30, 7, 21)

    return image, denoised_image

def extract_text_and_boxes(image, binary_image):
    boxes = pytesseract.image_to_data(binary_image, output_type=pytesseract.Output.DICT)
    n_boxes = len(boxes['level'])
    extracted_text = ""
    total_confidence = 0
    valid_boxes = 0

    for i in range(n_boxes):
        conf = int(boxes['conf'][i])
        if conf >= 60:  # Only consider boxes with a valid confidence level
            (x, y, w, h) = (boxes['left'][i], boxes['top'][i], boxes['width'][i], boxes['height'][i])
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            extracted_text += boxes['text'][i] + "\n"
            total_confidence += conf
            valid_boxes += 1

    average_confidence = total_confidence / valid_boxes if valid_boxes > 0 else 0
    return extracted_text.strip(), average_confidence

# Using an example
image_path = "pvx38c00-page06_2 copy.png"
original_image, binary_image = preprocess_image(image_path)
extracted_text, average_confidence = extract_text_and_boxes(original_image, binary_image)

# Print the extracted text and average confidence
print("Extracted Text:\n", extracted_text)
print("\nAverage Confidence Level:", average_confidence)

# Display the image with bounding boxes
cv2.imshow('Image with Bounding Boxes', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
