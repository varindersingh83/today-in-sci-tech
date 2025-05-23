"""
Tests for the alerts module.
"""

import pytest
from unittest.mock import patch, MagicMock
from today_in_sci_tech.alerts import send_sms_alert

@pytest.fixture
def mock_env_vars(monkeypatch):
    """Set up mock environment variables."""
    monkeypatch.setenv("ALERT_EMAIL", "test@example.com")
    monkeypatch.setenv("ALERT_EMAIL_PASS", "test_password")
    monkeypatch.setenv("ALERT_SMS_GATEWAY", "test@carrier.com")

def test_send_sms_alert_success(mock_env_vars):
    """Test successful SMS alert sending."""
    with patch('smtplib.SMTP_SSL') as mock_smtp_ssl:
        mock_server = MagicMock()
        mock_smtp_ssl.return_value.__enter__.return_value = mock_server
        
        send_sms_alert("Test Subject", "Test Body")
        
        # Verify SMTP was called correctly
        mock_smtp_ssl.assert_called_once_with("smtp.gmail.com", 465)
        mock_server.login.assert_called_once_with("test@example.com", "test_password")
        mock_server.sendmail.assert_called_once()

def test_send_sms_alert_emoji_handling(mock_env_vars):
    """Test that emojis are properly handled in the message."""
    with patch('smtplib.SMTP_SSL') as mock_smtp_ssl:
        mock_server = MagicMock()
        mock_smtp_ssl.return_value.__enter__.return_value = mock_server
        
        send_sms_alert("Test Subject 🚀", "Test Body with emoji 🎉")
        
        # Get the message that was sent
        call_args = mock_server.sendmail.call_args[0]
        message = call_args[2]
        
        # Verify emojis were removed
        assert "🚀" not in message
        assert "🎉" not in message

def test_send_sms_alert_error(mock_env_vars):
    """Test handling of SMTP errors."""
    with patch('smtplib.SMTP_SSL') as mock_smtp_ssl:
        mock_server = MagicMock()
        mock_server.login.side_effect = Exception("SMTP Error")
        mock_smtp_ssl.return_value.__enter__.return_value = mock_server
        
        # Should not raise exception, but print error
        send_sms_alert("Test Subject", "Test Body")
        
        # Verify SMTP was attempted
        mock_server.login.assert_called_once() 