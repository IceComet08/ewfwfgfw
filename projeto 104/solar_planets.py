import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sol",
             (100,80),
             cv2.FONT_HERSHEY_COMPLEX,
             2,
             (253, 233, 16)
             )

cv2.putText(img,
            "Mercurio",
             (110,180),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (112, 128, 144)
             )

cv2.putText(img,
            "Venus",
             (180,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (220, 20, 60)
             )

cv2.putText(img,
            "Terra",
             (300,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
            (123, 160, 91)
             )
cv2.putText(img,
            "Marte",
             (400,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (227, 38, 54)
             )
cv2.putText(img,
            "Jupiter",
             (480,90),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (205, 133, 63)
             )            
            
cv2.putText(img,
            "Saturno",
             (700,120),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255, 160, 122)
             ) 

cv2.putText(img,
            "Urano",
             (900,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
            (230, 230, 250)
             )

cv2.putText(img,
            "Netuno",
             (1100,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (0, 0, 128)
             )
cv2.waitKey(0)
cv2.imshow("resultado",img)
cv2.imwrite("Solar_systemwithname.jpg",img)