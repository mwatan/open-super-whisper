"""src.gui.components.dialogs.api_key_dialog

Azure OpenAI 設定用のダイアログ。

従来は OpenAI API キーのみを扱っていましたが、Azure OpenAI では
`Endpoint` と `api-version`（および必要に応じて `Deployment`）が必要なため、
それらもまとめて入力できるようにしています。
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QPushButton, QLineEdit, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt

from src.gui.resources.labels import AppLabels
from src.gui.resources.styles import AppStyles

class APIKeyDialog(QDialog):
    """
    Azure OpenAI 設定を入力するためのダイアログ
    
    APIキーの入力、保存、表示を管理するダイアログウィンドウ
    """
    
    def __init__(self, parent=None, api_key=None, endpoint=None, api_version=None, deployment=None):
        """
        APIKeyDialogの初期化
        
        Parameters
        ----------
        parent : QWidget, optional
            親ウィジェット
        api_key : str, optional
            初期表示する Azure OpenAI APIキー
        endpoint : str, optional
            初期表示する Azure OpenAI Endpoint
        api_version : str, optional
            初期表示する Azure OpenAI API Version
        deployment : str, optional
            初期表示する Deployment 名（任意）
        """
        super().__init__(parent)
        self.setWindowTitle(AppLabels.API_KEY_DIALOG_TITLE)
        self.setMinimumWidth(400)
        
        # スタイルシートを設定
        self.setStyleSheet(AppStyles.API_KEY_DIALOG_STYLE)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # APIキー入力
        form_layout = QFormLayout()
        form_layout.setSpacing(10)

        self.endpoint_input = QLineEdit()
        if endpoint:
            self.endpoint_input.setText(endpoint)
        self.endpoint_input.setPlaceholderText("https://{resource}.openai.azure.com/")
        form_layout.addRow(AppLabels.API_ENDPOINT_LABEL, self.endpoint_input)

        self.api_version_input = QLineEdit()
        if api_version:
            self.api_version_input.setText(api_version)
        self.api_version_input.setPlaceholderText("2024-02-15-preview")
        form_layout.addRow(AppLabels.API_VERSION_LABEL, self.api_version_input)

        self.deployment_input = QLineEdit()
        if deployment:
            self.deployment_input.setText(deployment)
        self.deployment_input.setPlaceholderText("(空でOK) 例: whisper-1")
        form_layout.addRow(AppLabels.API_DEPLOYMENT_LABEL, self.deployment_input)

        self.api_key_input = QLineEdit()
        if api_key:
            self.api_key_input.setText(api_key)
        self.api_key_input.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addRow(AppLabels.API_KEY_LABEL, self.api_key_input)
        
        layout.addLayout(form_layout)
        
        # 情報テキスト
        info_label = QLabel(AppLabels.API_KEY_INFO)
        info_label.setWordWrap(True)
        info_label.setStyleSheet(AppStyles.API_KEY_INFO_LABEL_STYLE)
        layout.addWidget(info_label)
        
        # ボタン
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        self.save_button = QPushButton(AppLabels.SAVE_BUTTON)
        self.save_button.clicked.connect(self.accept)
        
        self.cancel_button = QPushButton(AppLabels.CANCEL_BUTTON)
        self.cancel_button.setObjectName("cancelButton")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.save_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def get_api_key(self):
        """
        入力されたAPIキーを返す
        
        Returns
        -------
        str
            入力されたAPIキー
        """
        return self.api_key_input.text() 

    def get_endpoint(self):
        """入力された Azure OpenAI Endpoint を返す"""
        return self.endpoint_input.text().strip()

    def get_api_version(self):
        """入力された Azure OpenAI API Version を返す"""
        return self.api_version_input.text().strip()

    def get_deployment(self):
        """入力された Deployment 名（任意）を返す"""
        return self.deployment_input.text().strip()