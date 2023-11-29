# Diyet Listesi Hazırlama Botu

Bu Python programı, diyetisyenler tarafından müşterileri için özel diyet listeleri hazırlamak için kullanılır. Program danışanın boyuna, kilosuna, yaşına ve öğün sayısına göre en uygun diyet listesini bulup oluşturur ve belirtilen bilgilerle birlikte bir dosyaya kaydeder.

## Kullanım

Program bir kullanıcı arayüzü kullanmaktadır. Müşterinin adını, öğün sayısını, kilosunu, boyunu ve yaşını girdikten sonra, kullanıcı "Hesapla" düğmesine tıklayarak işlemi başlatır.

### Gerekli Kütüphaneler

- `tkinter`: Bir kullanıcı arayüzü oluşturmak için.
- `openpyxl`: Excel dosyalarını manipüle etmek için.
- `random`: Rastgele değerler üretmek için.
- os`: Dosya işlemleri ve işletim sistemi işlemleri için.
- `datetime`: Tarih ve saat işlemleri için.
- `docx`: Word dosyaları oluşturmak ve düzenlemek için.

## Nasıl Kullanılır

1. Programı çalıştırın.
2. Müşterinin adını, öğün sayısını, kilosunu, boyunu ve yaşını girin.
3. "Hesapla" düğmesine tıklayın.
4. Program müşteri için uygun diyet listesini oluşturur ve dosyaya kaydeder.

## Geliştirici Notları

Bu programın çalışması için önceden belirlenmiş diyet listeleri olmalıdır. Bu listeler öğün sayısına göre klasörlere ayrılmalı ve belirli bir düzene göre isimlendirilmelidir.

Projem, diyetisyenlerin müşterileri için özel diyet listeleri hazırlamalarını kolaylaştırmak için yazdığım bir Python programını içeriyor. Bu program kullanıcının boyuna, kilosuna, yaşına ve öğün sayısına göre ince hesaplamalar yapıyor ve önceden oluşturulmuş diyet listeleri arasından en uygun olanını seçerek danışanın bilgilerinin kayıtlı olduğu diyet dosyasına kaydediyor.

Programın çalışabilmesi için önceden belirlenmiş haftalık diyet listelerinin olması gerekmektedir. Bu listeler öğün sayısına göre 2 öğün ve 3 öğün olmak üzere iki sınıfa ayrılacaktır. Her sınıf içinde, her biri için en az 2 aylık klasörler olacaktır. Her ayın klasör adı BMI sınıflarını içeren klasörleri içerecektir: 21-25 BMI, 26-29 BMI, 30-33 BMI, 34-37 BMI ve üstü. Bu klasörler içerisinde 4 farklı haftalık diyet listesi bulunacaktır.

Örneğin, klasör sıralaması aşağıdaki gibi olacaktır: DIETS\THREE_MEAL_DIETS\AY2\21_25bmi\1.hafta.docx veya DIETS\TWO_MEAL_DIETS\AY2\26_29bmi\4.hafta.docx.

Diyet listeleri hazırlandıktan sonra program girilen danışan bilgilerine göre en uygun diyeti bulur, danışanın bilgileriyle birlikte listeyi oluşturur ve kaydeder.
