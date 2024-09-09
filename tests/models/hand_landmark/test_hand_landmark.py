# Reference: https://colab.research.google.com/github/googlesamples/mediapipe/blob/main/examples/hand_landmarker/python/hand_landmarker.ipynb

import pytest

dependencies = ["mediapipe"]


@pytest.mark.usefixtures("manage_dependencies")
@pytest.mark.compilation_xfail
def test_hand_landmark(record_property):
    record_property("model_name", "Hand Landmark")

    import mediapipe as mp
    from mediapipe.tasks import python
    from mediapipe.tasks.python import vision

    base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
    options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
    detector = vision.HandLandmarker.create_from_options(options)

    image = mp.Image.create_from_file("woman_hands.jpg")

    detection_result = detector.detect(image)

    record_property("torch_ttnn", (detector.detect, image, detection_result))
