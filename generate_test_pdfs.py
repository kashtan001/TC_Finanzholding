#!/usr/bin/env python3
"""
Скрипт для генерации всех тестовых PDF файлов для TC Finanzholding
Использует данные "12" для всех полей XXX
"""

import sys
import os

# Добавляем текущую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_costructor import (
    generate_contratto_pdf,
    generate_garanzia_pdf,
    generate_carta_pdf,
    generate_approvazione_pdf
)

def main():
    """Генерирует все тестовые PDF файлы с данными 12"""
    
    print("🚀 Генерируем тестовые PDF файлы для TC Finanzholding...")
    print("📝 Используем данные '12' для всех полей XXX")
    print("")
    
    # Тестовые данные с "12" для всех полей
    test_data_12 = {
        'name': '12',
        'amount': 12.0,
        'duration': 12,
        'tan': 12.0,
        'taeg': 12.0,
        'payment': 12.0
    }
    
    templates = [
        ('contratto', generate_contratto_pdf, test_data_12),
        ('garanzia', generate_garanzia_pdf, {'name': '12'}),
        ('carta', generate_carta_pdf, test_data_12),
        ('approvazione', generate_approvazione_pdf, test_data_12),
    ]
    
    generated_files = []
    
    for template_name, generator_func, data in templates:
        try:
            print(f"📄 Генерируем {template_name}...")
            
            if template_name == 'garanzia':
                buf = generator_func(data['name'])
            else:
                buf = generator_func(data)
            
            filename = f'test_{template_name}_12.pdf'
            
            with open(filename, 'wb') as f:
                f.write(buf.read())
            
            generated_files.append(filename)
            print(f"✅ {filename} создан успешно!")
            print("")
            
        except Exception as e:
            print(f"❌ Ошибка при генерации {template_name}: {e}")
            print("")
            import traceback
            traceback.print_exc()
    
    print("=" * 50)
    print("✅ Генерация завершена!")
    print("")
    print("📋 Созданные файлы:")
    for filename in generated_files:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"  - {filename} ({size:,} байт)")
        else:
            print(f"  - {filename} (не найден)")
    
    if not generated_files:
        print("  ⚠️ PDF файлы не созданы")

if __name__ == '__main__':
    main()

