$(function() {
    $('#WAButton').floatingWhatsApp({
      phone: '543513466657', //WhatsApp Business phone number International format-
      //Get it with Toky at https://toky.co/en/features/whatsapp.
      headerTitle: 'Chatea con nosotros en WhatsApps!', //Popup Title
      popupMessage: 'Hola, ¿Cómo puedo ayudarte?', //Popup Message
      showPopup: false, //Enables popup display
      buttonImage: '<img src="static/images/whatsapp.svg" />', //Button Image
      //headerColor: 'crimson', //Custom header color
      //backgroundColor: 'crimson', //Custom background button color
      position: "right"    
    });
});

