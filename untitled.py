<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="windowModality">
   <enum>Qt::NonModal</enum>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1130</width>
    <height>802</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>نظام سيارات</string>
  </property>
  <property name="layoutDirection">
   <enum>Qt::LeftToRight</enum>
  </property>
  <property name="styleSheet">
   <string notr="true">

background-image: url(:/car/BBBBB.jpg);

color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QTextBrowser" name="textBrowser">
   <property name="geometry">
    <rect>
     <x>225</x>
     <y>50</y>
     <width>771</width>
     <height>31</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>50</y>
     <width>93</width>
     <height>41</height>
    </rect>
   </property>
   <property name="accessibleName">
    <string/>
   </property>
   <property name="text">
    <string>بحث</string>
   </property>
   <property name="default">
    <bool>true</bool>
   </property>
   <property name="flat">
    <bool>false</bool>
   </property>
  </widget>
  <widget class="QFrame" name="frame">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>119</y>
     <width>791</width>
     <height>611</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true"/>
   </property>
   <property name="frameShape">
    <enum>QFrame::StyledPanel</enum>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Raised</enum>
   </property>
   <widget class="QTextEdit" name="textEdit">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>40</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_2">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>180</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_3">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>110</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_5">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>340</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_6">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>410</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_8">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>40</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_9">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>110</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_10">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>190</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_11">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>260</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_12">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>330</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_13">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>400</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit_14">
    <property name="geometry">
     <rect>
      <x>440</x>
      <y>40</y>
      <width>21</width>
      <height>431</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>652</x>
      <y>550</y>
      <width>101</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>اضافة معلومات</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>522</x>
      <y>550</y>
      <width>101</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>تعديل المعلومات</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_4">
    <property name="geometry">
     <rect>
      <x>222</x>
      <y>530</y>
      <width>111</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>مسح المعلومات</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>684</x>
      <y>50</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>رقم السيارة</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>680</x>
      <y>120</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>الشركة المالكة</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>680</x>
      <y>190</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>الفرع</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>680</x>
      <y>350</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>رقم القعادة</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>680</x>
      <y>420</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>رقم المحرك</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>50</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>نوع السيارة</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>120</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>موديل السيارة</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>200</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>حمولة السيارة</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_10">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>270</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>الوزن</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_11">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>340</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>الشكل</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_12">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>410</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>اللون</string>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox_2">
    <property name="geometry">
     <rect>
      <x>542</x>
      <y>270</y>
      <width>231</width>
      <height>31</height>
     </rect>
    </property>
    <property name="layoutDirection">
     <enum>Qt::RightToLeft</enum>
    </property>
    <item>
     <property name="text">
      <string>بيع</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>ايجار</string>
     </property>
    </item>
   </widget>
   <widget class="QComboBox" name="comboBox_3">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>490</y>
      <width>231</width>
      <height>31</height>
     </rect>
    </property>
    <property name="layoutDirection">
     <enum>Qt::RightToLeft</enum>
    </property>
    <item>
     <property name="text">
      <string>بنزين</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>غاز</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>ديزل</string>
     </property>
    </item>
   </widget>
  </widget>
  <widget class="QLabel" name="label_6">
   <property name="geometry">
    <rect>
     <x>870</x>
     <y>60</y>
     <width>121</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>ادخل رقم السيارة</string>
   </property>
  </widget>
  <widget class="QComboBox" name="comboBox">
   <property name="geometry">
    <rect>
     <x>832</x>
     <y>141</y>
     <width>271</width>
     <height>31</height>
    </rect>
   </property>
   <property name="layoutDirection">
    <enum>Qt::RightToLeft</enum>
   </property>
   <property name="currentText">
    <string>أختيار نوع الخدمة</string>
   </property>
   <item>
    <property name="text">
     <string>أختيار نوع الخدمة</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>أضافه سيارة</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>الوقود</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>الصيانة</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>التراخيص</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>الايرادات</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>الايجارات</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>الكهرباء</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>التقارير</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>المستخدمين</string>
    </property>
   </item>
  </widget>
  <zorder>frame</zorder>
  <zorder>textBrowser</zorder>
  <zorder>pushButton</zorder>
  <zorder>label_6</zorder>
  <zorder>comboBox</zorder>
 </widget>
 <resources>
  <include location="C:/Users/hp/Desktop/BBBBB.qrc"/>
 </resources>
 <connections/>
</ui>
