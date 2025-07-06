import sys
import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ExamAdmitCard(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("UNIVERSITY OF UYO, UYO")
        self.setGeometry(100, 100, 200, 400)

        main_layout = qtw.QVBoxLayout()
        main_layout.setSpacing(10)

        # === Header Text: University + Class Admit Card ===
        university_label = qtw.QLabel("UNIVERSITY OF UYO, UYO")
        university_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        university_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        admit_label = qtw.QLabel("CLASS ADMIT CARD")
        admit_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        admit_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Stack labels with minimal spacing
        text_header = qtw.QVBoxLayout()
        text_header.setSpacing(2)  # 👈 reduce vertical space
        text_header.setContentsMargins(0, 0, 0, 0)
        text_header.addWidget(university_label)
        text_header.addWidget(admit_label)

        # === Photo Box on the right ===
        photo_label = qtw.QLabel()
        photo_label.setFixedSize(100, 100)
        photo_label.setStyleSheet("border: 1px solid black;")

        # === Combine Header Row: Text + Photo ===
        header_row = qtw.QHBoxLayout()

        header_row.addStretch()
        header_row.addLayout(text_header)
        header_row.addStretch()
        header_row.addWidget(photo_label, alignment=Qt.AlignmentFlag.AlignTop)

        main_layout.addLayout(header_row)

        # === Info Grid ===
        grid = qtw.QGridLayout()
        grid.setSpacing(10)
        font = QFont("Arial", 12)

        labels = [
            ("Name Of Student:", 0, 0),
            ("Sex:", 0, 1),
            ("Reg. No:", 0, 2),
            ("Department:", 1, 0),
            ("Faculty:", 1, 1),
            ("Session:", 2, 0),
            ("Semester:", 2, 1),
            ("Years Of Student:", 2, 2),
        ]

        for text, row, col in labels:
            lbl = qtw.QLabel(text)
            lbl.setFont(font)
            grid.addWidget(lbl, row, col)

        # === Course Code Section ===
        grid.addWidget(qtw.QLabel("Course Code(I): ____________________"), 4, 0)
        for i in range(2, 11):  # (II) to (X)
            row = 4 + (i - 1) // 3
            col = (i - 1) % 3
            code_label = qtw.QLabel(f"({i}) ____________________")
            code_label.setFont(font)
            grid.addWidget(code_label, row, col)

        main_layout.addLayout(grid)

        # === Signature Section ===
        sig_layout = qtw.QHBoxLayout()
        sig_layout.setSpacing(50)
        for sig in ["Student's Signature", "FO's Signature", "H.O.D Signature"]:
            sig_label = qtw.QLabel(f"{'_'*20}\n{sig}")
            sig_label.setFont(font)
            sig_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            sig_layout.addWidget(sig_label)

        main_layout.addStretch()
        main_layout.addLayout(sig_layout)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = ExamAdmitCard()
    window.show()
    sys.exit(app.exec())
