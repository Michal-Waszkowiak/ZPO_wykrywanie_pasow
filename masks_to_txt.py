import os
import cv2

input_dir = 'tmp\masks'
output_dir = 'tmp\labels'

os.makedirs(output_dir, exist_ok=True)

for mask_file in os.listdir(input_dir):
    image_path = os.path.join(input_dir, mask_file)
    
    mask = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    H, W = mask.shape
    
    unique_classes = set(mask.flatten())
    unique_classes.discard(0)  # Usuń background, jeśli obecny

    with open('{}.txt'.format(os.path.join(output_dir, mask_file)[:-4]), 'w') as f:
        for class_id in unique_classes:
            class_mask = (mask == class_id).astype('uint8')
            contours, _ = cv2.findContours(class_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            for cnt in contours:
                if cv2.contourArea(cnt) > 200:
                    polygon = []
                    for point in cnt:
                        x, y = point[0]
                        polygon.append(x / W)
                        polygon.append(y / H)
                    
                    f.write(f"{class_id} ")
                    f.write(" ".join(map(str, polygon)))
                    f.write("\n")
