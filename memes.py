import os
import random

import cv2
import numpy as np

import config


def create_drake_meme(top_msg, bottom_msg):
    tmp = ""
    gap = 0
    img = cv2.imread(config.MEMES_URL.get("drake"))
    for i, el in enumerate(top_msg):
        tmp += el
        if len(tmp) == 15:
            cv2.putText(
                img,
                tmp,
                (340, 50 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
            tmp = ""
            gap += 40
        if i == len(top_msg) - 1:
            cv2.putText(
                img,
                tmp,
                (340, 50 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
    tmp = ""
    gap = 0
    for i, el in enumerate(bottom_msg):
        tmp += el
        if len(tmp) == 15:
            cv2.putText(
                img,
                tmp,
                (340, 250 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
            tmp = ""
            gap += 40
        if i == len(bottom_msg) - 1:
            cv2.putText(
                img,
                tmp,
                (340, 250 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
    img_name = "drake_" + str(random.randint(1, 100000)) + ".jpg"
    cv2.imwrite(os.path.join(config.CREATED_MEMES_FOLDER, img_name), img)
    return img_name


def create_doge_meme(top_msg, bottom_msg):
    tmp = ""
    gap = 0
    img = cv2.imread(config.MEMES_URL.get("doge"))
    for i, el in enumerate(top_msg):
        tmp += el
        if len(tmp) == 18:
            cv2.putText(
                img,
                tmp,
                (280, 50 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
            tmp = ""
            gap += 40
        if i == len(top_msg) - 1:
            cv2.putText(
                img,
                tmp,
                (280, 50 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
    tmp = ""
    gap = 0
    for i, el in enumerate(bottom_msg):
        tmp += el
        if len(tmp) == 14:
            cv2.putText(
                img,
                tmp,
                (300, 360 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
            tmp = ""
            gap += 40
        if i == len(bottom_msg) - 1:
            cv2.putText(
                img,
                tmp,
                (300, 360 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
    img_name = "doge_" + str(random.randint(1, 100000)) + ".jpg"
    cv2.imwrite(os.path.join(config.CREATED_MEMES_FOLDER, img_name), img)
    return img_name


def create_sqrt_meme(msg):
    tmp = ""
    gap = 0
    img = cv2.imread(config.MEMES_URL.get("sqrt"))
    for i, el in enumerate(msg):
        tmp += el
        if len(tmp) == 12:
            cv2.putText(
                img,
                tmp,
                (200, 550 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
            tmp = ""
            gap += 40
        if i == len(msg) - 1:
            cv2.putText(
                img,
                tmp,
                (200, 550 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
    img_name = "sqrt_" + str(random.randint(1, 100000)) + ".jpg"
    cv2.imwrite(os.path.join(config.CREATED_MEMES_FOLDER, img_name), img)
    return img_name


def create_supermind_meme(first_msg, second_msg, third_msg, four_msg):
    tmp = ""
    gap = 0
    img = cv2.imread(config.MEMES_URL.get("supermind"))
    for i, el in enumerate(first_msg):
        tmp += el
        if len(tmp) == 15:
            cv2.putText(
                img,
                tmp,
                (50, 50 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
            tmp = ""
            gap += 40
        if i == len(first_msg) - 1:
            cv2.putText(
                img,
                tmp,
                (50, 50 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
    tmp = ""
    gap = 0
    for i, el in enumerate(second_msg):
        tmp += el
        if len(tmp) == 15:
            cv2.putText(
                img,
                tmp,
                (50, 230 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
            tmp = ""
            gap += 40
        if i == len(second_msg) - 1:
            cv2.putText(
                img,
                tmp,
                (50, 230 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
    tmp = ""
    gap = 0
    for i, el in enumerate(third_msg):
        tmp += el
        if len(tmp) == 15:
            cv2.putText(
                img,
                tmp,
                (50, 420 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
            tmp = ""
            gap += 40
        if i == len(third_msg) - 1:
            cv2.putText(
                img,
                tmp,
                (50, 420 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
    tmp = ""
    gap = 0
    for i, el in enumerate(four_msg):
        tmp += el
        if len(tmp) == 15:
            cv2.putText(
                img,
                tmp,
                (50, 615 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
            tmp = ""
            gap += 40
        if i == len(four_msg) - 1:
            cv2.putText(
                img,
                tmp,
                (50, 615 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
    img_name = "supermind_" + str(random.randint(1, 100000)) + ".jpg"
    cv2.imwrite(os.path.join(config.CREATED_MEMES_FOLDER, img_name), img)
    return img_name


def create_lazy_meme(msg):
    tmp = ""
    gap = 0
    img = cv2.imread(config.MEMES_URL.get("lazy"))
    for i, el in enumerate(msg):
        tmp += el
        if len(tmp) == 30:
            cv2.putText(
                img,
                tmp,
                (50, 50 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
            tmp = ""
            gap += 40
        if i == len(msg) - 1:
            cv2.putText(
                img,
                tmp,
                (50, 50 + gap),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
            )
    img_name = "lazy_" + str(random.randint(1, 100000)) + ".jpg"
    cv2.imwrite(os.path.join(config.CREATED_MEMES_FOLDER, img_name), img)
    return img_name
