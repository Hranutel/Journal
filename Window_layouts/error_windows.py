from PyQt5.QtWidgets import QMessageBox,QWidget,QListWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QScrollArea
from Window_layouts.main_window_layout import Icon,basic_font,title_font,list_font,Qt

#Not enough information error
not_enough_information_error = QMessageBox()
not_enough_information_error.addButton(QMessageBox.StandardButton.Ok)
not_enough_information_error.button(QMessageBox.StandardButton.Ok).setMinimumSize(180,20)
not_enough_information_error.button(QMessageBox.StandardButton.Ok).setMaximumSize(180,20)
not_enough_information_error.button(QMessageBox.StandardButton.Ok).setFont(basic_font)
not_enough_information_error.resize(300,350)
not_enough_information_error.setFont(basic_font)
not_enough_information_error.setWindowIcon(Icon)
not_enough_information_error.setObjectName("main_window")

#Student exists error
student_exists_error = QMessageBox()
student_exists_error.addButton(QMessageBox.StandardButton.Ok)
student_exists_error.button(QMessageBox.StandardButton.Ok).setMinimumSize(180,20)
student_exists_error.button(QMessageBox.StandardButton.Ok).setMaximumSize(180,20)
student_exists_error.button(QMessageBox.StandardButton.Ok).setFont(basic_font)
student_exists_error.resize(300,350)
student_exists_error.setFont(basic_font)
student_exists_error.setWindowIcon(Icon)
student_exists_error.setObjectName("main_window")

#Unselected student error
unselected_student_error = QMessageBox()
unselected_student_error.addButton(QMessageBox.StandardButton.Ok)
unselected_student_error.button(QMessageBox.StandardButton.Ok).setMinimumSize(180,20)
unselected_student_error.button(QMessageBox.StandardButton.Ok).setMaximumSize(180,20)
unselected_student_error.button(QMessageBox.StandardButton.Ok).setFont(basic_font)
unselected_student_error.resize(300,350)
unselected_student_error.setFont(basic_font)
unselected_student_error.setWindowIcon(Icon)
unselected_student_error.setObjectName("main_window")

#Entered incorrect type of information error
entered_incorrect_type_of_information_error = QMessageBox()
entered_incorrect_type_of_information_error.addButton(QMessageBox.StandardButton.Ok)
entered_incorrect_type_of_information_error.button(QMessageBox.StandardButton.Ok).setMinimumSize(180,20)
entered_incorrect_type_of_information_error.button(QMessageBox.StandardButton.Ok).setMaximumSize(180,20)
entered_incorrect_type_of_information_error.button(QMessageBox.StandardButton.Ok).setFont(basic_font)
entered_incorrect_type_of_information_error.resize(300,350)
entered_incorrect_type_of_information_error.setFont(basic_font)
entered_incorrect_type_of_information_error.setWindowIcon(Icon)
entered_incorrect_type_of_information_error.setObjectName("main_window")

#Entered incorrect date error
entered_incorrect_date_error = QMessageBox()
entered_incorrect_date_error.addButton(QMessageBox.StandardButton.Ok)
entered_incorrect_date_error.button(QMessageBox.StandardButton.Ok).setMinimumSize(180,20)
entered_incorrect_date_error.button(QMessageBox.StandardButton.Ok).setMaximumSize(180,20)
entered_incorrect_date_error.button(QMessageBox.StandardButton.Ok).setFont(basic_font)
entered_incorrect_date_error.resize(300,350)
entered_incorrect_date_error.setFont(basic_font)
entered_incorrect_date_error.setWindowIcon(Icon)
entered_incorrect_date_error.setObjectName("main_window")

#Entered incorrect weekday error
entered_incorrect_weekday_error = QMessageBox()
entered_incorrect_weekday_error.addButton(QMessageBox.StandardButton.Ok)
entered_incorrect_weekday_error.button(QMessageBox.StandardButton.Ok).setMinimumSize(180,20)
entered_incorrect_weekday_error.button(QMessageBox.StandardButton.Ok).setMaximumSize(180,20)
entered_incorrect_weekday_error.button(QMessageBox.StandardButton.Ok).setFont(basic_font)
entered_incorrect_weekday_error.resize(350,350)
entered_incorrect_weekday_error.setFont(basic_font)
entered_incorrect_weekday_error.setWindowIcon(Icon)
entered_incorrect_weekday_error.setObjectName("main_window")

#Entered incorrect time amount error
entered_incorrect_time_amount_error = QMessageBox()
entered_incorrect_time_amount_error.addButton(QMessageBox.StandardButton.Ok)
entered_incorrect_time_amount_error.button(QMessageBox.StandardButton.Ok).setMinimumSize(180,20)
entered_incorrect_time_amount_error.button(QMessageBox.StandardButton.Ok).setMaximumSize(180,20)
entered_incorrect_time_amount_error.button(QMessageBox.StandardButton.Ok).setFont(basic_font)
entered_incorrect_time_amount_error.resize(350,350)
entered_incorrect_time_amount_error.setFont(basic_font)
entered_incorrect_time_amount_error.setWindowIcon(Icon)
entered_incorrect_time_amount_error.setObjectName("main_window")

#Student has this lesson error
student_has_this_lesson_error = QMessageBox()
student_has_this_lesson_error.addButton(QMessageBox.StandardButton.Ok)
student_has_this_lesson_error.button(QMessageBox.StandardButton.Ok).setMinimumSize(180,20)
student_has_this_lesson_error.button(QMessageBox.StandardButton.Ok).setMaximumSize(180,20)
student_has_this_lesson_error.button(QMessageBox.StandardButton.Ok).setFont(basic_font)
student_has_this_lesson_error.resize(350,350)
student_has_this_lesson_error.setFont(basic_font)
student_has_this_lesson_error.setWindowIcon(Icon)
student_has_this_lesson_error.setObjectName("main_window")

#Warning windows
#Student remove warning 
student_remove_warning = QMessageBox()
student_remove_warning.addButton(QMessageBox.StandardButton.Ok)
student_remove_warning.button(QMessageBox.StandardButton.Ok).setMinimumSize(180,20)
student_remove_warning.button(QMessageBox.StandardButton.Ok).setMaximumSize(180,20)
student_remove_warning.button(QMessageBox.StandardButton.Ok).setFont(basic_font)
student_remove_warning.addButton(QMessageBox.StandardButton.Cancel)
student_remove_warning.button(QMessageBox.StandardButton.Cancel).setMinimumSize(180,20)
student_remove_warning.button(QMessageBox.StandardButton.Cancel).setMaximumSize(180,20)
student_remove_warning.button(QMessageBox.StandardButton.Cancel).setFont(basic_font)
student_remove_warning.resize(300,350)
student_remove_warning.setFont(basic_font)
student_remove_warning.setWindowIcon(Icon)
student_remove_warning.setObjectName("main_window")

#Lesson remove warning
#Student remove warning 
lesson_remove_warning = QMessageBox()
lesson_remove_warning.addButton(QMessageBox.StandardButton.Ok)
lesson_remove_warning.button(QMessageBox.StandardButton.Ok).setMinimumSize(180,20)
lesson_remove_warning.button(QMessageBox.StandardButton.Ok).setMaximumSize(180,20)
lesson_remove_warning.button(QMessageBox.StandardButton.Ok).setFont(basic_font)
lesson_remove_warning.addButton(QMessageBox.StandardButton.Cancel)
lesson_remove_warning.button(QMessageBox.StandardButton.Cancel).setMinimumSize(180,20)
lesson_remove_warning.button(QMessageBox.StandardButton.Cancel).setMaximumSize(180,20)
lesson_remove_warning.button(QMessageBox.StandardButton.Cancel).setFont(basic_font)
lesson_remove_warning.resize(300,350)
lesson_remove_warning.setFont(basic_font)
lesson_remove_warning.setWindowIcon(Icon)
lesson_remove_warning.setObjectName("main_window")

#Add student to joint lesson warning
add_student_to_joint_lesson_warning = QWidget()
add_student_to_joint_lesson_warning.resize(500,500)
add_student_to_joint_lesson_warning.setWindowIcon(Icon)
add_student_to_joint_lesson_warning.setObjectName("main_window")
##Add student to joint lesson warning layout
add_student_warning_title = QLabel("This lesson already exists, add the student to a joint lesson with:?")
add_student_warning_title.setFont(title_font)
###Scroll area
Scroll_students_layout = QVBoxLayout()
Scroll_students_window = QWidget()
Scroll_students_window.setLayout(Scroll_students_layout)
Scroll_students_window.setObjectName("lesson_window")
Scroll_students_area = QScrollArea()
Scroll_students_area.setWidget(Scroll_students_window)
Scroll_students_area.setWidgetResizable(True)
Scroll_students_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
Scroll_students_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
agree_button = QPushButton("Add")
agree_button.setMinimumSize(180,20)
agree_button.setMaximumSize(180,20)
agree_button.setFont(basic_font)
disagree_button = QPushButton("Cancel")
disagree_button.setMinimumSize(180,20) 
disagree_button.setMaximumSize(180,20) 
disagree_button.setFont(basic_font) 
buttons_layout = QHBoxLayout()
buttons_layout.addStretch(1)
buttons_layout.addWidget(agree_button)
buttons_layout.addStretch(2)
buttons_layout.addWidget(disagree_button)
buttons_layout.addStretch(1)
Add_student_to_joint_lesson_warning_layout = QVBoxLayout()
Add_student_to_joint_lesson_warning_layout.addWidget(add_student_warning_title,alignment=Qt.AlignHCenter)
Add_student_to_joint_lesson_warning_layout.addWidget(Scroll_students_area,alignment=Qt.AlignHCenter)
Add_student_to_joint_lesson_warning_layout.addLayout(buttons_layout)

add_student_to_joint_lesson_warning.setLayout(Add_student_to_joint_lesson_warning_layout)