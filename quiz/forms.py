from django import forms

CHOISES1 = [
('','Valitse vastaus'),
(1,'2011'),
(0,'2012'),
(0,'2014'),
]
CHOISES2 = [
('','Valitse vastaus'),
(1,'Malmin kauppaoppilaitoksella'),
(0,'Malmin palloiluhallissa'),
(0,'Mankkaan palloiluhallissa'),
]
CHOISES3 = [
('','Valitse vastaus'),
(0,'Lapuan Kobrat'),
(1,'Kauhajoen Karhut'),
(0,'MaSu Basket'),
]
CHOISES4 = [
('','Valitse vastaus'),
(0,'21.10.2019'),
(0,'19.9.2019'),
(1,'17.08.2019'),
]
CHOISES5 = [
('','Valitse vastaus'),
(0,'Viherpiipertäjän koulu'),
(0,'Muumilaakson koulu'),
(1,'Viherlaakson koulu'),
]
class SubmitForm(forms.Form):
    ans1 = forms.TypedChoiceField(choices=CHOISES1, empty_value=None, coerce=int, label='<br>Kysymys 1: <br> Minä vuonna Asi ja Janne tapasivat?')
    ans2 = forms.TypedChoiceField(choices=CHOISES2, empty_value=None, coerce=int, label='<br>Kysymys 2: <br> Missä he tapasivat ensimmäisen kerran?')
    ans3 = forms.TypedChoiceField(choices=CHOISES3, empty_value=None, coerce=int, label='<br>Kysymys 3: <br> Mitä joukkuetta Janne valmentaa?')
    ans4 = forms.TypedChoiceField(choices=CHOISES4, empty_value=None, coerce=int, label='<br>Kysymys 4: <br> Minä päivänä he menivät kihloihin?')
    ans5 = forms.TypedChoiceField(choices=CHOISES5, empty_value=None, coerce=int, label='<br>Kysymys 5: <br> Missä koulussa Asi toimii opettajana?')
    # ans6 = forms.ChoiceField(choices=CHOISES1, label='Anna vastaus?', required=False)
    # ans7 = forms.ChoiceField(choices=CHOISES1, label='Vastaa kysymykseen?', required=False)
    # ans8 = forms.ChoiceField(choices=CHOISES1, label='Anna vastaus?', required=False)
