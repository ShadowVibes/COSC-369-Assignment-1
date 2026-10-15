% COSC 369 - Prolog Knowledge Base

:- discontiguous course_section/2.
:- discontiguous teaches/2.
:- discontiguous teaches_section/2.
:- discontiguous course_title/2.
:- discontiguous class_schedule/5.
:- discontiguous meets_on/2.
:- discontiguous office_hours/3.
:- discontiguous faculty_member/1.
:- discontiguous faculty_department/2.
:- discontiguous faculty_email/2.
:- discontiguous faculty_office/2.
:- discontiguous faculty_appointment/2.

% Course information

course_section('CTEC 350.170', 'CTEC 350').
teaches('Adedoyin, Anthony', 'CTEC 350').
teaches_section('Adedoyin, Anthony', 'CTEC 350.170').
course_title('CTEC 350', 'Prin & Meth of Intru Det & Pre').
class_schedule('CTEC 350.170', 'MW', '16:00', '18:50', '108').
meets_on('CTEC 350.170', 'monday').
meets_on('CTEC 350.170', 'wednesday').

course_section('CTEC 350.180', 'CTEC 350').
teaches('Adedoyin, Anthony', 'CTEC 350').
teaches_section('Adedoyin, Anthony', 'CTEC 350.180').
course_title('CTEC 350', 'Prin & Meth of Intru Det & Pre').
class_schedule('CTEC 350.180', 'MW', '16:00', '18:50', '108').
meets_on('CTEC 350.180', 'monday').
meets_on('CTEC 350.180', 'wednesday').

course_section('CTEC 435.170', 'CTEC 435').
teaches('Adedoyin, Anthony', 'CTEC 435').
teaches_section('Adedoyin, Anthony', 'CTEC 435.170').
course_title('CTEC 435', 'UNIX System Administration').
class_schedule('CTEC 435.170', 'MW', '19:00', '21:50', '108').
meets_on('CTEC 435.170', 'monday').
meets_on('CTEC 435.170', 'wednesday').

course_section('CTEC 120.171', 'CTEC 120').
teaches('Agboli, P.', 'CTEC 120').
teaches_section('Agboli, P.', 'CTEC 120.171').
course_title('CTEC 120', 'Prin of SecureCoding Using Jav').
class_schedule('CTEC 120.171', 'MW', '17:00', '19:00', '201/112').
meets_on('CTEC 120.171', 'monday').
meets_on('CTEC 120.171', 'wednesday').

course_section('CTEC 300.170', 'CTEC 300').
teaches('Agboli, P.', 'CTEC 300').
teaches_section('Agboli, P.', 'CTEC 300.170').
course_title('CTEC 300', 'Database Achitecture').
class_schedule('CTEC 300.170', 'MW', '19:00', '21:50', '112').
meets_on('CTEC 300.170', 'monday').
meets_on('CTEC 300.170', 'wednesday').

course_section('CTEC 214.180', 'CTEC 214').
teaches('Baptiste, R.', 'CTEC 214').
teaches_section('Baptiste, R.', 'CTEC 214.180').
course_title('CTEC 214', 'Client Operating Systs').
class_schedule('CTEC 214.180', 'TR', '12:00', '15:40', '109').
meets_on('CTEC 214.180', 'tuesday').
meets_on('CTEC 214.180', 'thursday').

course_section('CTEC 302.170', 'CTEC 302').
teaches('Baptiste, R.', 'CTEC 302').
teaches_section('Baptiste, R.', 'CTEC 302.170').
course_title('CTEC 302', 'Computer Networking').
class_schedule('CTEC 302.170', 'TR', '16:00', '18:50', 'Dept').
meets_on('CTEC 302.170', 'tuesday').
meets_on('CTEC 302.170', 'thursday').

course_section('CTEC 302.180', 'CTEC 302').
teaches('Baptiste, R.', 'CTEC 302').
teaches_section('Baptiste, R.', 'CTEC 302.180').
course_title('CTEC 302', 'Computer Networking').
class_schedule('CTEC 302.180', 'TR', '16:00', '18:50', '111').
meets_on('CTEC 302.180', 'tuesday').
meets_on('CTEC 302.180', 'thursday').

course_section('CTEC 128.170', 'CTEC 128').
teaches('Bemley', 'CTEC 128').
teaches_section('Bemley', 'CTEC 128.170').
course_title('CTEC 128', 'Discrete Structures - Big Data').
class_schedule('CTEC 128.170', 'TR', '12:00', '14:50', 'Online').
meets_on('CTEC 128.170', 'tuesday').
meets_on('CTEC 128.170', 'thursday').

course_section('CTEC 298.180', 'CTEC 298').
teaches('Bemley, J', 'CTEC 298').
teaches_section('Bemley, J', 'CTEC 298.180').
course_title('CTEC 298', 'Symbolic Computation use BigDa').
class_schedule('CTEC 298.180', 'TR', '16:00', '18:50', '108').
meets_on('CTEC 298.180', 'tuesday').
meets_on('CTEC 298.180', 'thursday').

course_section('CTEC 671.555', 'CTEC 671').
teaches('Bemley, Jesse', 'CTEC 671').
teaches_section('Bemley, Jesse', 'CTEC 671.555').
course_title('CTEC 671', 'Smart Integrated Systems').
class_schedule('CTEC 671.555', 'TR', '16:00', '18:50', 'Online').
meets_on('CTEC 671.555', 'tuesday').
meets_on('CTEC 671.555', 'thursday').

course_section('CTEC 711.555', 'CTEC 711').
teaches('Ruth Agada', 'CTEC 711').
teaches_section('Ruth Agada', 'CTEC 711.555').
course_title('CTEC 711', 'IoT Capstone I').
class_schedule('CTEC 711.555', 'MWF', '17:00', '17:00', 'Online').
meets_on('CTEC 711.555', 'monday').
meets_on('CTEC 711.555', 'wednesday').
meets_on('CTEC 711.555', 'friday').

course_section('CTEC 720.555', 'CTEC 720').
teaches('Bright, Marvin', 'CTEC 720').
teaches_section('Bright, Marvin', 'CTEC 720.555').
course_title('CTEC 720', 'Master''s Thesis Research I').
class_schedule('CTEC 720.555', 'MW', '19:00', '21:50', 'Online').
meets_on('CTEC 720.555', 'monday').
meets_on('CTEC 720.555', 'wednesday').

course_section('CTEC 721.555', 'CTEC 721').
teaches('Bright, Marvin', 'CTEC 721').
teaches_section('Bright, Marvin', 'CTEC 721.555').
course_title('CTEC 721', 'Master''s Thesis Research II').
class_schedule('CTEC 721.555', 'TR', '19:00', '09:50', 'Online').
meets_on('CTEC 721.555', 'tuesday').
meets_on('CTEC 721.555', 'thursday').

course_section('CTEC 424.555', 'CTEC 424').
teaches('Carter, Adrian D.', 'CTEC 424').
teaches_section('Carter, Adrian D.', 'CTEC 424.555').
course_title('CTEC 424', 'Database Administration').
class_schedule('CTEC 424.555', 'TR', '19:00', '21:50', 'Online').
meets_on('CTEC 424.555', 'tuesday').
meets_on('CTEC 424.555', 'thursday').

course_section('CTEC 445.170', 'CTEC 445').
teaches('Carter, Adrian D.', 'CTEC 445').
teaches_section('Carter, Adrian D.', 'CTEC 445.170').
course_title('CTEC 445', 'Fund of Cryptography & Applica').
class_schedule('CTEC 445.170', 'MW', '16:00', '18:50', '111').
meets_on('CTEC 445.170', 'monday').
meets_on('CTEC 445.170', 'wednesday').

course_section('CTEC 450.170', 'CTEC 450').
teaches('Carter, Adrian D.', 'CTEC 450').
teaches_section('Carter, Adrian D.', 'CTEC 450.170').
course_title('CTEC 450', 'Case Studies in Comp Security').
class_schedule('CTEC 450.170', 'MW', '19:00', '21:50', '111').
meets_on('CTEC 450.170', 'monday').
meets_on('CTEC 450.170', 'wednesday').

course_section('CTEC 305.170', 'CTEC 305').
teaches('Chery, Pierrot', 'CTEC 305').
teaches_section('Chery, Pierrot', 'CTEC 305.170').
course_title('CTEC 305', 'Server Administration I').
class_schedule('CTEC 305.170', 'TR', '16:00', '18:50', 'Dept').
meets_on('CTEC 305.170', 'tuesday').
meets_on('CTEC 305.170', 'thursday').

course_section('CTEC 305.180', 'CTEC 305').
teaches('Chery, Pierrot', 'CTEC 305').
teaches_section('Chery, Pierrot', 'CTEC 305.180').
course_title('CTEC 305', 'Server Administration I').
class_schedule('CTEC 305.180', 'TR', '16:00', '18:50', '109').
meets_on('CTEC 305.180', 'tuesday').
meets_on('CTEC 305.180', 'thursday').

course_section('CTEC 405.170', 'CTEC 405').
teaches('Chery, Pierrot', 'CTEC 405').
teaches_section('Chery, Pierrot', 'CTEC 405.170').
course_title('CTEC 405', 'Server Administration II').
class_schedule('CTEC 405.170', 'TR', '19:00', '21:50', '109').
meets_on('CTEC 405.170', 'tuesday').
meets_on('CTEC 405.170', 'thursday').

course_section('CTEC 226.180', 'CTEC 226').
teaches('Deal, Shawn', 'CTEC 226').
teaches_section('Deal, Shawn', 'CTEC 226.180').
course_title('CTEC 226', 'Intro To Db Development').
class_schedule('CTEC 226.180', 'TR', '19:00', '21:50', '116').
meets_on('CTEC 226.180', 'tuesday').
meets_on('CTEC 226.180', 'thursday').

course_section('CTEC 294.170', 'CTEC 294').
teaches('Dixon, Carl', 'CTEC 294').
teaches_section('Dixon, Carl', 'CTEC 294.170').
course_title('CTEC 294', 'PC Architecture').
class_schedule('CTEC 294.170', 'MW', '16:00', '18:50', '112').
meets_on('CTEC 294.170', 'monday').
meets_on('CTEC 294.170', 'wednesday').

course_section('CTEC 294.180', 'CTEC 294').
teaches('Dixon, Carl', 'CTEC 294').
teaches_section('Dixon, Carl', 'CTEC 294.180').
course_title('CTEC 294', 'PC Architecture').
class_schedule('CTEC 294.180', 'MW', '16:00', '18:50', '112').
meets_on('CTEC 294.180', 'monday').
meets_on('CTEC 294.180', 'wednesday').

course_section('CTEC 120.170', 'CTEC 120').
teaches('Dr. Stone, D. B.', 'CTEC 120').
teaches_section('Dr. Stone, D. B.', 'CTEC 120.170').
course_title('CTEC 120', 'Prin of SecureCoding Using Jav').
class_schedule('CTEC 120.170', 'MW', '12:00', '03:15', '116').
meets_on('CTEC 120.170', 'monday').
meets_on('CTEC 120.170', 'wednesday').

course_section('CTEC 125.555', 'CTEC 125').
teaches('Dr. Stone, D. B.', 'CTEC 125').
teaches_section('Dr. Stone, D. B.', 'CTEC 125.555').
course_title('CTEC 125', 'Intro to Python programming').
class_schedule('CTEC 125.555', 'Unknown', 'On-line Asynchronous Course', 'Unknown', 'Online').

course_section('CTEC 125.556', 'CTEC 125').
teaches('Dr. Stone, D. B.', 'CTEC 125').
teaches_section('Dr. Stone, D. B.', 'CTEC 125.556').
course_title('CTEC 125', 'Intro to Python programming').
class_schedule('CTEC 125.556', 'Unknown', 'On-line Asynchronous Course', 'Unknown', 'Online').

course_section('CTEC 324.555', 'CTEC 324').
teaches('Dr. Stone, D. B.', 'CTEC 324').
teaches_section('Dr. Stone, D. B.', 'CTEC 324.555').
course_title('CTEC 324', 'Database Appl Dev').
class_schedule('CTEC 324.555', 'MW', '16:00', '18:50', 'online').
meets_on('CTEC 324.555', 'monday').
meets_on('CTEC 324.555', 'wednesday').

course_section('CTEC 111.172', 'CTEC 111').
teaches('Eugene Harris', 'CTEC 111').
teaches_section('Eugene Harris', 'CTEC 111.172').
course_title('CTEC 111', 'Cybersecurity for All').
class_schedule('CTEC 111.172', 'TR', '08:00', '10:50', '111').
meets_on('CTEC 111.172', 'tuesday').
meets_on('CTEC 111.172', 'thursday').

course_section('CTEC 114.172', 'CTEC 114').
teaches('Eugene T. Harris', 'CTEC 114').
teaches_section('Eugene T. Harris', 'CTEC 114.172').
course_title('CTEC 114', 'Comp Tools & Environ').
class_schedule('CTEC 114.172', 'TR', '16:00', '18:50', '114').
meets_on('CTEC 114.172', 'tuesday').
meets_on('CTEC 114.172', 'thursday').

course_section('CTEC 475.180', 'CTEC 475').
teaches('Francis, Wilbert R.', 'CTEC 475').
teaches_section('Francis, Wilbert R.', 'CTEC 475.180').
course_title('CTEC 475', 'Cloud Computing').
class_schedule('CTEC 475.180', 'MW', '19:00', '21:50', '114').
meets_on('CTEC 475.180', 'monday').
meets_on('CTEC 475.180', 'wednesday').

course_section('CTEC 111.173', 'CTEC 111').
teaches('Henri E. Cooper', 'CTEC 111').
teaches_section('Henri E. Cooper', 'CTEC 111.173').
course_title('CTEC 111', 'Cybersecurity for All').
class_schedule('CTEC 111.173', 'MW', '16:00', '18:50', 'Online').
meets_on('CTEC 111.173', 'monday').
meets_on('CTEC 111.173', 'wednesday').

course_section('CTEC 111.171', 'CTEC 111').
teaches('Staphord Bengesi', 'CTEC 111').
teaches_section('Staphord Bengesi', 'CTEC 111.171').
course_title('CTEC 111', 'Cybersecurity for All').
class_schedule('CTEC 111.171', 'MW', '08:00', '10:50', 'Online').
meets_on('CTEC 111.171', 'monday').
meets_on('CTEC 111.171', 'wednesday').

course_section('CTEC 393.555', 'CTEC 393').
teaches('Lamar, Courtney', 'CTEC 393').
teaches_section('Lamar, Courtney', 'CTEC 393.555').
course_title('CTEC 393', 'Internet Prog II').
class_schedule('CTEC 393.555', 'MW', '16:00', '18:50', 'Online').
meets_on('CTEC 393.555', 'monday').
meets_on('CTEC 393.555', 'wednesday').

course_section('CTEC 426.170', 'CTEC 426').
teaches('Miller, Stephanie R.', 'CTEC 426').
teaches_section('Miller, Stephanie R.', 'CTEC 426.170').
course_title('CTEC 426', 'Expert Systems Using Big Data').
class_schedule('CTEC 426.170', 'MW', '19:00', '21:50', '114').
meets_on('CTEC 426.170', 'monday').
meets_on('CTEC 426.170', 'wednesday').

course_section('CTEC 651.555', 'CTEC 651').
teaches('Njeh, Felix', 'CTEC 651').
teaches_section('Njeh, Felix', 'CTEC 651.555').
course_title('CTEC 651', 'Internet of Things of Digital Res').
class_schedule('CTEC 651.555', 'MW', '16:00', '18:50', 'Online').
meets_on('CTEC 651.555', 'monday').
meets_on('CTEC 651.555', 'wednesday').

course_section('CTEC 410.170', 'CTEC 410').
teaches('Okonofua, Henry', 'CTEC 410').
teaches_section('Okonofua, Henry', 'CTEC 410.170').
course_title('CTEC 410', 'Internet Technology').
class_schedule('CTEC 410.170', 'TR', '16:00', '18:50', '201').
meets_on('CTEC 410.170', 'tuesday').
meets_on('CTEC 410.170', 'thursday').

course_section('CTEC 410.180', 'CTEC 410').
teaches('Okonofua, Henry', 'CTEC 410').
teaches_section('Okonofua, Henry', 'CTEC 410.180').
course_title('CTEC 410', 'Internet Technology').
class_schedule('CTEC 410.180', 'TR', '16:00', '18:50', '201').
meets_on('CTEC 410.180', 'tuesday').
meets_on('CTEC 410.180', 'thursday').

course_section('CTEC 222.170', 'CTEC 222').
teaches('Roberts, Curtis', 'CTEC 222').
teaches_section('Roberts, Curtis', 'CTEC 222.170').
course_title('CTEC 222', 'Linux Operating System').
class_schedule('CTEC 222.170', 'TR', '19:00', '21:50', '108').
meets_on('CTEC 222.170', 'tuesday').
meets_on('CTEC 222.170', 'thursday').

course_section('CTEC 335.170', 'CTEC 335').
teaches('Roberts, Curtis', 'CTEC 335').
teaches_section('Roberts, Curtis', 'CTEC 335.170').
course_title('CTEC 335', 'Network Protocols').
class_schedule('CTEC 335.170', 'TR', '16:00', '18:50', '116').
meets_on('CTEC 335.170', 'tuesday').
meets_on('CTEC 335.170', 'thursday').

course_section('CTEC 335.180', 'CTEC 335').
teaches('Roberts, Curtis', 'CTEC 335').
teaches_section('Roberts, Curtis', 'CTEC 335.180').
course_title('CTEC 335', 'Network Protocols').
class_schedule('CTEC 335.180', 'TR', '16:00', '18:50', '116').
meets_on('CTEC 335.180', 'tuesday').
meets_on('CTEC 335.180', 'thursday').

course_section('CTEC 345.170', 'CTEC 345').
teaches('Brett Tolbert', 'CTEC 345').
teaches_section('Brett Tolbert', 'CTEC 345.170').
course_title('CTEC 345', 'Found of Comp and Network Secu').
class_schedule('CTEC 345.170', 'MW', '17:00', '19:50', '109').
meets_on('CTEC 345.170', 'monday').
meets_on('CTEC 345.170', 'wednesday').

course_section('CTEC 345.180', 'CTEC 345').
teaches('Brett Tolbert', 'CTEC 345').
teaches_section('Brett Tolbert', 'CTEC 345.180').
course_title('CTEC 345', 'Found of Comp and Network Secu').
class_schedule('CTEC 345.180', 'MW', '17:00', '19:50', '111').
meets_on('CTEC 345.180', 'monday').
meets_on('CTEC 345.180', 'wednesday').

course_section('CTEC 402.170', 'CTEC 402').
teaches('Staphord Bengesi', 'CTEC 402').
teaches_section('Staphord Bengesi', 'CTEC 402.170').
course_title('CTEC 402', 'Software and OS Security').
class_schedule('CTEC 402.170', 'MW', '19:00', '21:50', 'Online').
meets_on('CTEC 402.170', 'monday').
meets_on('CTEC 402.170', 'wednesday').

course_section('CTEC 402.180', 'CTEC 402').
teaches('Ruth Agada', 'CTEC 402').
teaches_section('Ruth Agada', 'CTEC 402.180').
course_title('CTEC 402', 'Software and OS Security').
class_schedule('CTEC 402.180', 'MW', '19:00', '21:50', 'Online').
meets_on('CTEC 402.180', 'monday').
meets_on('CTEC 402.180', 'wednesday').

course_section('CTEC 435.180', 'CTEC 435').
teaches('Ruth Agada', 'CTEC 435').
teaches_section('Ruth Agada', 'CTEC 435.180').
course_title('CTEC 435', 'UNIX System Administration').
class_schedule('CTEC 435.180', 'MW', '19:00', '21:50', '108').
meets_on('CTEC 435.180', 'monday').
meets_on('CTEC 435.180', 'wednesday').

course_section('CTEC 445.180', 'CTEC 445').
teaches('Staphord Bengesi', 'CTEC 445').
teaches_section('Staphord Bengesi', 'CTEC 445.180').
course_title('CTEC 445', 'Fund of Cryptography & Applica').
class_schedule('CTEC 445.180', 'MW', '16:00', '18:50', '109').
meets_on('CTEC 445.180', 'monday').
meets_on('CTEC 445.180', 'wednesday').

course_section('CTEC 450.180', 'CTEC 450').
teaches('Loubna Dali', 'CTEC 450').
teaches_section('Loubna Dali', 'CTEC 450.180').
course_title('CTEC 450', 'Case Studies in Comp Security').
class_schedule('CTEC 450.180', 'MW', '19:00', '21:50', '111').
meets_on('CTEC 450.180', 'monday').
meets_on('CTEC 450.180', 'wednesday').

course_section('CTEC 111.170', 'CTEC 111').
teaches('Loubna Dali', 'CTEC 111').
teaches_section('Loubna Dali', 'CTEC 111.170').
course_title('CTEC 111', 'Cybersecurity for All').
class_schedule('CTEC 111.170', 'TR', '09:00', '11:50', 'Online').
meets_on('CTEC 111.170', 'tuesday').
meets_on('CTEC 111.170', 'thursday').

course_section('CTEC 220.170', 'CTEC 220').
teaches('Vega, J.', 'CTEC 220').
teaches_section('Vega, J.', 'CTEC 220.170').
course_title('CTEC 220', 'Adv Secure Coding Using Java').
class_schedule('CTEC 220.170', 'MW', '11:00', '13:50', '114').
meets_on('CTEC 220.170', 'monday').
meets_on('CTEC 220.170', 'wednesday').

course_section('CTEC 220.180', 'CTEC 220').
teaches('Vega, J.', 'CTEC 220').
teaches_section('Vega, J.', 'CTEC 220.180').
course_title('CTEC 220', 'Adv Secure Coding Using Java').
class_schedule('CTEC 220.180', 'MW', '11:00', '13:50', '114').
meets_on('CTEC 220.180', 'monday').
meets_on('CTEC 220.180', 'wednesday').

course_section('CTEC 230.180', 'CTEC 230').
teaches('Vega, J.', 'CTEC 230').
teaches_section('Vega, J.', 'CTEC 230.180').
course_title('CTEC 230', 'Application of Data Structures').
class_schedule('CTEC 230.180', 'MW', '16:00', '18:50', '114').
meets_on('CTEC 230.180', 'monday').
meets_on('CTEC 230.180', 'wednesday').

course_section('CTEC 114.170', 'CTEC 114').
teaches('Victoria Lee', 'CTEC 114').
teaches_section('Victoria Lee', 'CTEC 114.170').
course_title('CTEC 114', 'Comp Tools & Environ').
class_schedule('CTEC 114.170', 'MW', '16:00', '18:50', '116').
meets_on('CTEC 114.170', 'monday').
meets_on('CTEC 114.170', 'wednesday').

course_section('CTEC 128.180', 'CTEC 128').
teaches('Wilson, Marcella J.', 'CTEC 128').
teaches_section('Wilson, Marcella J.', 'CTEC 128.180').
course_title('CTEC 128', 'Discrete Structures - Big Data').
class_schedule('CTEC 128.180', 'TR', '16:00', '18:50', 'Online').
meets_on('CTEC 128.180', 'tuesday').
meets_on('CTEC 128.180', 'thursday').

course_section('CTEC 230.170', 'CTEC 230').
teaches('Wilson, Marcella J.', 'CTEC 230').
teaches_section('Wilson, Marcella J.', 'CTEC 230.170').
course_title('CTEC 230', 'Application of Data Structures').
class_schedule('CTEC 230.170', 'TR', '11:00', '14:40', '114').
meets_on('CTEC 230.170', 'tuesday').
meets_on('CTEC 230.170', 'thursday').

course_section('CTEC 293.170', 'CTEC 293').
teaches('Wilson, Marcella J.', 'CTEC 293').
teaches_section('Wilson, Marcella J.', 'CTEC 293.170').
course_title('CTEC 293', 'Edge Technology').
class_schedule('CTEC 293.170', 'MW', '16:00', '18:50', '114').
meets_on('CTEC 293.170', 'monday').
meets_on('CTEC 293.170', 'wednesday').

course_section('CTEC 415.180', 'CTEC 415').
teaches('Wilson, Marcella J.', 'CTEC 415').
teaches_section('Wilson, Marcella J.', 'CTEC 415.180').
course_title('CTEC 415', 'Edge Computing').
class_schedule('CTEC 415.180', 'TR', '10:00', '12:50', '114').
meets_on('CTEC 415.180', 'tuesday').
meets_on('CTEC 415.180', 'thursday').

course_section('COSC 369', 'COSC 369').
teaches('Dr. Appolo Tankeh', 'COSC 369').
teaches_section('Dr. Appolo Tankeh', 'COSC 369').
course_title('COSC 369', 'Software Engineering I').
class_schedule('COSC 369', 'TR', '09:30', '10:45', 'CS 108').
meets_on('COSC 369', 'tuesday').
meets_on('COSC 369', 'thursday').

% Syllabus faculty information

faculty_member('Dr. Appolo Tankeh').
faculty_email('Dr. Appolo Tankeh', 'atankeh@bowiestate.edu').
faculty_office('Dr. Appolo Tankeh', 'CS 108').
syllabus_office_hours('Tue/Thursday: 10:45-1pm').
office_hours('Dr. Appolo Tankeh', 'tuesday', 'Tue/Thursday: 10:45-1pm').
office_hours('Dr. Appolo Tankeh', 'thursday', 'Tue/Thursday: 10:45-1pm').

% Faculty CSV information

faculty_member('Adedoyin, Anthony').
faculty_department('Adedoyin, Anthony', 'Computer Science & Technology').
faculty_email('Adedoyin, Anthony', 'aadedoyin@bowiestate.edu').
office_hours('Adedoyin, Anthony', 'monday', '13:00-14:30').
office_hours('Adedoyin, Anthony', 'wednesday', '13:00-14:30').

faculty_member('Agboli, P.').
faculty_department('Agboli, P.', 'Computer Science & Technology').
office_hours('Agboli, P.', 'tuesday', '11:00-12:30').
office_hours('Agboli, P.', 'thursday', '11:00-12:30').

faculty_member('Baptiste, R.').
faculty_department('Baptiste, R.', 'Computer Science & Technology').

faculty_member('Bemley').
faculty_department('Bemley', 'Computer Science & Technology').
office_hours('Bemley', 'friday', '10:00-11:30').

faculty_member('Bemley, J').
faculty_department('Bemley, J', 'Computer Science & Technology').
office_hours('Bemley, J', 'monday', '13:00-14:30').
office_hours('Bemley, J', 'wednesday', '13:00-14:30').

faculty_member('Bemley, Jesse').
faculty_department('Bemley, Jesse', 'Computer Science & Technology').
faculty_email('Bemley, Jesse', 'jbemley@bowiestate.edu').

faculty_member('Ruth Agada').
faculty_department('Ruth Agada', 'Computer Science & Technology').
faculty_email('Ruth Agada', 'ragada@bowiestate.edu').
office_hours('Ruth Agada', 'wednesday', '14:00-15:30').

faculty_member('Bright, Marvin').
faculty_department('Bright, Marvin', 'Computer Science & Technology').
faculty_email('Bright, Marvin', 'mbright@bowiestate.edu').
office_hours('Bright, Marvin', 'friday', '10:00-11:30').

faculty_member('Carter, Adrian D.').
faculty_department('Carter, Adrian D.', 'Computer Science & Technology').
faculty_email('Carter, Adrian D.', 'acarter@bowiestate.edu').
office_hours('Carter, Adrian D.', 'monday', '13:00-14:30').
office_hours('Carter, Adrian D.', 'wednesday', '13:00-14:30').

faculty_member('Chery, Pierrot').
faculty_department('Chery, Pierrot', 'Computer Science & Technology').
faculty_email('Chery, Pierrot', 'pchery@bowiestate.edu').
office_hours('Chery, Pierrot', 'tuesday', '11:00-12:30').
office_hours('Chery, Pierrot', 'thursday', '11:00-12:30').

faculty_member('Deal, Shawn').
faculty_department('Deal, Shawn', 'Computer Science & Technology').
faculty_email('Deal, Shawn', 'sdeal@bowiestate.edu').
office_hours('Deal, Shawn', 'wednesday', '14:00-15:30').

faculty_member('Dixon, Carl').
faculty_department('Dixon, Carl', 'Computer Science & Technology').
faculty_email('Dixon, Carl', 'cdixon@bowiestate.edu').
office_hours('Dixon, Carl', 'friday', '10:00-11:30').

faculty_member('Dr. Stone, D. B.').
faculty_department('Dr. Stone, D. B.', 'Computer Science & Technology').

faculty_member('Eugene Harris').
faculty_department('Eugene Harris', 'Computer Science & Technology').
faculty_email('Eugene Harris', 'eharris@bowiestate.edu').
office_hours('Eugene Harris', 'tuesday', '11:00-12:30').
office_hours('Eugene Harris', 'thursday', '11:00-12:30').

faculty_member('Eugene T. Harris').
faculty_department('Eugene T. Harris', 'Computer Science & Technology').
office_hours('Eugene T. Harris', 'wednesday', '14:00-15:30').

faculty_member('Francis, Wilbert R.').
faculty_department('Francis, Wilbert R.', 'Computer Science & Technology').
faculty_email('Francis, Wilbert R.', 'wfrancis@bowiestate.edu').
office_hours('Francis, Wilbert R.', 'friday', '10:00-11:30').

faculty_member('Henri E. Cooper').
faculty_department('Henri E. Cooper', 'Computer Science & Technology').
faculty_email('Henri E. Cooper', 'hcooper@bowiestate.edu').
office_hours('Henri E. Cooper', 'monday', '13:00-14:30').
office_hours('Henri E. Cooper', 'wednesday', '13:00-14:30').

faculty_member('Staphord Bengesi').
faculty_department('Staphord Bengesi', 'Computer Science & Technology').
faculty_email('Staphord Bengesi', 'sbengesi@bowiestate.edu').

faculty_member('Lamar, Courtney').
faculty_department('Lamar, Courtney', 'Computer Science & Technology').
faculty_email('Lamar, Courtney', 'clamar@bowiestate.edu').
office_hours('Lamar, Courtney', 'wednesday', '14:00-15:30').

faculty_member('Miller, Stephanie R.').
faculty_department('Miller, Stephanie R.', 'Computer Science & Technology').
faculty_email('Miller, Stephanie R.', 'smiller@bowiestate.edu').
office_hours('Miller, Stephanie R.', 'friday', '10:00-11:30').


% Prolog rules

teaches_course(P, C) :- teaches(P, C).
professor_courses(P, C) :- teaches(P, C).
section_instructor(S, P) :- teaches_section(P, S).

course_on_day(C, D) :-
    course_section(S, C),
    meets_on(S, D).

professor_teaches_on(P, D) :-
    teaches_section(P, S),
    meets_on(S, D).

professor_office_hours(P, D, H) :-
    office_hours(P, D, H).

faculty_search(Search, P) :-
    faculty_member(P),
    downcase_atom(Search, L),
    downcase_atom(P, LP),
    sub_atom(LP, _, _, _, L).

professor_email(P, E) :- faculty_email(P, E).
professor_office(P, O) :- faculty_office(P, O).
professor_department(P, D) :- faculty_department(P, D).
