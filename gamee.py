import tkinter as tk
from tkinter import messagebox
import math
import threading
import time

# Kích thước ban đầu của hình tròn
circle_radius = 50

# Vị trí ban đầu của hình tròn
circle_x, circle_y = 200, 200

# Kích thước ban đầu của hình tròn thứ hai
circle_radius_2 = 50

# Vị trí ban đầu của hình tròn thứ hai
circle_x_2, circle_y_2 = 100, 100

# Hàm để di chuyển hình tròn và thay đổi kích thước
def move_and_adjust_circles(event):
    global circle_radius, circle_x, circle_y, circle_radius_2, circle_x_2, circle_y_2, notification_displayed
    key = event.keysym
    if key == "Left" and circle_x - circle_radius > 0:
        circle_x -= 10
    elif key == "Right" and circle_x + circle_radius < window_width:
        circle_x += 10
    elif key == "Up" and circle_y - circle_radius > 0:
        circle_y -= 10
    elif key == "Down" and circle_y + circle_radius < window_height:
        circle_y += 10
    elif key == "k":
        circle_radius += 10
    elif key == "m" and circle_radius > 10:
        circle_radius -= 10
    elif key == "a" and circle_x_2 - circle_radius_2 > 0:
        circle_x_2 -= 10
    elif key == "d" and circle_x_2 + circle_radius_2 < window_width:
        circle_x_2 += 10
    elif key == "w" and circle_y_2 - circle_radius_2 > 0:
        circle_y_2 -= 10
    elif key == "s" and circle_y_2 + circle_radius_2 < window_height:
        circle_y_2 += 10
    elif key == "i":
        circle_radius_2 += 10
    elif key == "h" and circle_radius_2 > 10:
        circle_radius_2 -= 10

    # Kiểm tra xem hai hình tròn có chạm nhau không
    distance = math.sqrt((circle_x - circle_x_2) ** 2 + (circle_y - circle_y_2) ** 2)

    if distance < (circle_radius + circle_radius_2) and not notification_displayed:
        # Nếu chạm nhau và thông báo chưa được hiển thị, hiển thị thông báo
        notification_thread = threading.Thread(target=display_notification)
        notification_thread.start()

        # Đẩy hai hình tròn ra xa nhau
        angle = math.atan2(circle_y_2 - circle_y, circle_x_2 - circle_x)
        circle_x -= 20 * math.cos(angle)
        circle_y -= 20 * math.sin(angle)
        circle_x_2 += 20 * math.cos(angle)
        circle_y_2 += 20 * math.sin(angle)
    elif distance >= (circle_radius + circle_radius_2) and notification_displayed:
        # Nếu không chạm nhau và thông báo đã được hiển thị, xóa thông báo và thiết lập lại biến kiểm tra
        canvas.delete("message")
        notification_displayed = False

    # Cập nhật vị trí và kích thước của hình tròn thứ nhất
    canvas.coords(circle, circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius,
                  circle_y + circle_radius)
    canvas.coords(label, circle_x, circle_y)

    # Cập nhật vị trí và kích thước của hình tròn thứ hai
    canvas.coords(circle_2, circle_x_2 - circle_radius_2, circle_y_2 - circle_radius_2, circle_x_2 + circle_radius_2,
                  circle_y_2 + circle_radius_2)
    canvas.coords(label_2, circle_x_2, circle_y_2)

# Hàm để hiển thị thông báo và tự động ẩn nó sau 3 giây
def display_notification():
    global notification_displayed
    canvas.create_text(200, 350, text="Chạm nhau", fill="red", tags="message")
    notification_displayed = True
    time.sleep(3)  # Đợi 3 giây
    canvas.delete("message")
    notification_displayed = False

# Tạo cửa sổ tkinter
root = tk.Tk()
root.title("Hoàng Thuận")

# Đặt màu nền của cửa sổ thành màu vàng
root.configure(bg="yellow")

# Kích thước của cửa sổ
window_width, window_height = 400, 400

# Tạo canvas để vẽ hình tròn
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="yellow")
canvas.pack()

# Vẽ hình tròn màu đỏ
circle = canvas.create_oval(circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius,
                            circle_y + circle_radius, fill="red")

# Tạo nhãn để hiển thị tên
label = canvas.create_text(circle_x, circle_y, text="Hình Tròn Đỏ", fill="white")

# Vẽ hình tròn màu xanh
circle_2 = canvas.create_oval(circle_x_2 - circle_radius_2, circle_y_2 - circle_radius_2, circle_x_2 + circle_radius_2,
                              circle_y_2 + circle_radius_2, fill="blue")

# Tạo nhãn để hiển thị tên
label_2 = canvas.create_text(circle_x_2, circle_y_2, text="Hình Tròn Xanh", fill="white")

# Biến kiểm tra để xác định xem thông báo đã hiển thị hay chưa
notification_displayed = False

# Bắt sự kiện nhấn phím
root.bind("<Key>", move_and_adjust_circles)

# Đặt focus vào cửa sổ để bắt đầu nhận sự kiện từ bàn phím
canvas.focus_set()

# Chạy ứng dụng tkinter
root.mainloop()
