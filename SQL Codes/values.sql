INSERT INTO doctors(
    first_name,
    last_name,
    specialization,
    contact_number)
VALUES
('Atsumu', 'Miya', 'Psychiatry', '6461115454'),
('Osamu', 'Miya', 'Internal Medicine', '6461115456'),
('Satoru', 'Gojo', 'Cardiology', '6462221314'),
('Chuuya', 'Nakahara', 'Pediatrics', '6461211218');

INSERT INTO patients(
    first_name,
    last_name,
    date_of_birth,
    primary_doctor_id,
    contact_number)
VALUES
('Kita', 'Shinsuke', '2000-02-16', 1, '6462211259'),
('Kageyama', 'Tobio', '2000-05-07', 2, '6461514547'),
('Hinata', 'Shouyo', '2000-10-10', 2, '9175451122'),
('Suna', 'Rinatro', '2000-12-18', 3, '9174488545');
