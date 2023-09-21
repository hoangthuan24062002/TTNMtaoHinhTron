import tkinter as tk
import math

# Kích thước ban đầu của hình tròn
circle_radius = 50

# Vị trí ban đầu của hình tròn
circle_x, circle_y = 200, 200

# Kích thước ban đầu của hình tròn thứ hai
circle_radius_2 = 50

# Vị trí ban đầu của hình tròn thứ hai
circle_x_2, circle_y_2 = 100, 100

# Biến để kiểm tra xem thông báo đã được hiển thị hay chưa
notification_displayed = False


# Hàm để di chuyển hình tròn và thay đổi kích thước
def move_and_adjust_circles(event):
    global circle_radius, circle_x, circle_y, circle_radius_2, circle_x_2, circle_y_2, notification_displayed
    key = event.keysym
    if key == "Left":
        circle_x -= 10
    elif key == "Right":
        circle_x += 10
    elif key == "Up":
        circle_y -= 10
    elif key == "Down":
        circle_y += 10
    elif key == "k":
        circle_radius += 10
    elif key == "m" and circle_radius > 10:
        circle_radius -= 10
    elif key == "a":
        circle_x_2 -= 10
    elif key == "d":
        circle_x_2 += 10
    elif key == "w":
        circle_y_2 -= 10
    elif key == "s":
        circle_y_2 += 10
    elif key == "i":
        circle_radius_2 += 10
    elif key == "h" and circle_radius_2 > 10:
        circle_radius_2 -= 10

    # Kiểm tra xem hai hình tròn có chạm nhau không
    distance = math.sqrt((circle_x - circle_x_2) ** 2 + (circle_y - circle_y_2) ** 2)

    if distance < (circle_radius + circle_radius_2) and not notification_displayed:
        # Nếu chạm nhau và thông báo chưa được hiển thị, hiển thị thông báo
        canvas.create_text(200, 350, text="cxzc", fill="red", tags="message")
        notification_displayed = True

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


# Tạo cửa sổ tkinter
root = tk.Tk()
root.title("Di chuyển và điều chỉnh kích thước hai hình tròn")

# Tạo canvas để vẽ hình tròn
canvas = tk.Canvas(root, width=400, height=400)
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

# Bắt sự kiện nhấn phím
root.bind("<Key>", move_and_adjust_circles)

# Đặt focus vào cửa sổ để bắt đầu nhận sự kiện từ bàn phím
canvas.focus_set()

# Chạy ứng dụng tkinter
root.mainloop()
