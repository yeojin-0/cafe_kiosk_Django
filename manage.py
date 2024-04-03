#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cafe_Django.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

# python manage.py runserver


# Question -> 음료 종류(아메리카종류, 라떼, 차, 에이드)
# Choice -> 세부 음료 종류
# startproject하고
# 요구사항 분석하고
# 테이블 만들기까지
# 스레드에 깃허브 주소 공유하기