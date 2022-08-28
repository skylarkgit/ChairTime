import argparse
import torch

from yolov5_face.detect_face import detect_one, load_model

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str,
                        default='runs/train/exp5/weights/last.pt', help='model.pt path(s)')
    parser.add_argument('--img-size', type=int, default=640,
                        help='inference size (pixels)')
    opt = parser.parse_args()
    print(opt)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    device = "cpu"
    model = load_model(opt.weights, device)

    detect_one(model, './frame1.jpg', device)
