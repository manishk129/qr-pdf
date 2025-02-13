import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import shutil
from typing import List, Optional


class QrCode:
    """
    Represents a QR code with a given value.

    Attributes:
        value (str): The data to encode in the QR code.
        img (qrcode.image.pil.PilImage): The generated QR code image.
    """

    def __init__(self, value: str) -> None:
        """
        Initializes a QrCode instance.

        Args:
            value (str): The data to encode in the QR code.
        """
        self.value = value
        self.img = self.generate_qr_code()

    def generate_qr_code(self) -> object:
        """
        Generates a QR code image using the specified value.

        Returns:
            object: The generated QR code image.
        """
        qr = qrcode.QRCode(version=5,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=10, border=4)
        qr.add_data(self.value)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        return img


class QRCodeOnSheet:
    """
    Generates a PDF file with multiple QR codes arranged in a grid.

    Attributes:
        values (List[str]): List of data values to be encoded as QR codes.
        rows_count (int): Number of rows in the grid.
        cols_count (int): Number of columns in the grid.
        file_name (Optional[str]): Name of the output PDF file.
        margin (int): Margin percentage around the QR codes.
        padding (int): Padding percentage between QR codes.
    """

    def __init__(self, values: List[str], rows_count: int = 1,
                 cols_count: int = 1, file_name: Optional[str] = None,
                 margin: int = 5, padding: int = 4) -> None:
        """
        Initializes a QRCodeOnSheet instance.

        Args:
            values (List[str]): List of data values to be encoded as QR codes.
            rows_count (int): Number of rows in the grid (default is 1).
            cols_count (int): Number of columns in the grid (default is 1).
            file_name (Optional[str]): Name of the output PDF file (default is None).
            margin (int): Margin percentage around the QR codes (default is 5).
            padding (int): Padding percentage between QR codes (default is 4).
        """
        self.values = values
        self.rows_count = rows_count
        self.cols_count = cols_count
        self.file_name = file_name
        self.margin = margin  # in percentage
        self.padding = padding

    def save_qr_to_file(self, file: Optional[str] = None) -> None:
        """
        Saves the QR codes to a PDF file.

        Args:
            file (Optional[str]): The name of the output PDF file. If None,
            uses the initialized file_name.
        """
        if file:
            self.file_name = file
        c = canvas.Canvas(self.file_name, pagesize=A4)

        # Clean up and prepare temporary directory for QR code images
        if os.path.exists('temp') and os.path.isdir('temp'):
            shutil.rmtree('temp')
        os.mkdir('temp')

        # Generate QR codes either in a grid or one per page
        if self.cols_count == 1 and self.rows_count == 1:
            self.__generate_on_each_page(c)
        else:
            self.__generate_in_matrix(c)

        # Clean up temporary directory
        if os.path.exists('temp') and os.path.isdir('temp'):
            shutil.rmtree('temp')

        c.save()

    def __generate_in_matrix(self, c: canvas.Canvas) -> None:
        """
        Generates QR codes in a grid format on the PDF.

        Args:
            c (canvas.Canvas): The canvas on which the QR codes will be drawn.
        """
        width, height = A4
        qr_box_width = ((1 - 2 * (self.margin / 100)) * width) / self.cols_count
        qr_box_height = ((1 - 2 * (self.margin / 100)) * height) / \
                        self.rows_count
        qr_width = qr_box_width * (1 - 2 * (self.padding / 100))
        qr_height = qr_box_height * (1 - 2 * (self.padding / 100))
        qr_height = qr_width = min(qr_height, qr_width)

        curr_count = 0
        page_count = 0
        each_page_qrs_cnt = self.cols_count * self.rows_count

        for qr_code_value in self.values:
            row = (curr_count - page_count * each_page_qrs_cnt) // \
                  self.cols_count
            col = (curr_count - page_count * each_page_qrs_cnt) % \
                  self.cols_count

            x_offset = (self.margin / 100) * width + col * qr_box_width + (
                    qr_box_width - qr_width) / 2
            y_offset = (self.margin / 100) * height + (self.rows_count - row
                                                       - 1) * qr_box_height + (
                               qr_box_height - qr_height) / 2

            qr_img = QrCode(qr_code_value)
            qr_img.img.save(f'temp/{qr_code_value}.png', format="PNG")
            c.drawImage(f'temp/{qr_code_value}.png', x_offset, y_offset,
                        qr_width, qr_height)
            c.saveState()
            curr_count += 1

            # Move to a new page when the current page is full
            if curr_count >= (self.rows_count * self.cols_count) and (
                    curr_count) % (self.rows_count * self.cols_count) == 0:
                page_count += 1
                c.showPage()

    def __generate_on_each_page(self, c: canvas.Canvas) -> None:
        """
        Generates one QR code per page on the PDF.

        Args:
            c (canvas.Canvas): The canvas on which the QR codes will be drawn.
        """
        width, height = A4
        qr_width = (1 - 2 * (self.margin / 100)) * width
        qr_height = (1 - 2 * (self.margin / 100)) * height
        qr_height = qr_width = min(qr_height, qr_width)
        x_offset = (width - qr_width) / 2
        y_offset = (height - qr_height) / 2

        for qr_code_value in self.values:
            qr_img = QrCode(qr_code_value)
            qr_img.img.save(f'temp/{qr_code_value}.png', format="PNG")
            c.drawImage(f'temp/{qr_code_value}.png', x_offset, y_offset,
                        qr_width, qr_height)
            c.saveState()
            c.showPage()
