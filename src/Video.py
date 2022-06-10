import cv2 as cv


from process.detect_objects import draw_connected_components, get_connected_components


class Video:

    def __init__(self, path: str):
        self.path = path
        self.cap = cv.VideoCapture(self.path, apiPreference=cv.CAP_FFMPEG)
        self.data = {
            "connected_components_per_frame": [],
        }

        if not self.cap.isOpened():
            print(f"No se pudo abrir el vídeo \"{self.path}\"")
            exit(1)

    def numOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def __str__(self) -> str:
        return self.path

    def reset(self):
        self.cap.set(cv.CAP_PROP_POS_FRAMES, 0)


    def process(self, showContours: bool = False):
        print("Procesando vídeo...")

        cap = self.cap
        self.data["connected_components"] = []  # Reset contours_per_frame

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Detect objects
            cc = get_connected_components(frame)
            self.data["connected_components_per_frame"].append(cc)

            # Draw contours
            if showContours:
                drawed = frame.copy()
                draw_connected_components(drawed, cc)
                cv.imshow("CC", drawed)
                if cv.waitKey() & 0xFF == ord('q'):
                    break

        
        if (showContours):
            cv.destroyAllWindows()
        print("Vídeo procesado")

