const askQuestionModal = document.getElementById('askQuestion');
const thankQuestionModal = document.getElementById('thankQuestion');
const questionErrorModal = document.getElementById('questionError');



function copyEmail() {
    event.preventDefault();
    const email = "itfriendly_corporative.gmail.com";
    navigator.clipboard.writeText(email);
}

function openAccountModal(){
    event.preventDefault();
const accountWindow = document.getElementById('account');
const currentPath = window.location.href;
console.log(currentPath + 'get_user_studies')
   $.ajax({
       url: currentPath + 'get_user_studies',
       type: 'GET',
       dataType: 'json',
       success: function (response){
           const data = response.data;
           console.log(data)
           const modalContent = $('#courses');
           modalContent.empty();
           for (let i = 0; i < data.length; i++){
               modalContent.append('<p id="faq_a">' + data[i] + '</p>');
           }
           accountWindow.style.display = 'block';
       }
})

}


function closeThankQuestionModal(){
    thankQuestionModal.style.display = 'none';
}

function closeQuestionErrorModal(){
    questionErrorModal.style.display = 'none';
}

function openAskQuestion(){
    event.preventDefault();
    askQuestionModal.style.display = 'block';
}

function closeAskQuestion() {
    askQuestionModal.style.display = 'none';
}

function openThankQuestionModal() {
    thankQuestionModal.style.display = 'block';
}

function openQuestionErrorModal(){
    questionErrorModal.style.display = 'block';
}

$('#askQuestionForm').submit(function(event){
    event.preventDefault();
    let formData = $(this).serialize();
    $.ajax({
        type: 'POST',
        url: 'ask_question',
        data: formData,
        dataType: 'json'
    })
        .done(function (response){
            if (response.success === true){
                console.log('success')
                closeAskQuestion();
                openThankQuestionModal();
            }else {
                openQuestionErrorModal();
                var modalContent = $('#new_content');
                modalContent.empty();
                console.log(response.errors)
                for (var i = 0; i < response.errors.length; i++) {
                    modalContent.append('<h2 id="faq_q">' + response.errors[i] + '</h2>');
                }
            }
        });
    });

  function getFAQ(){
    const faqWindow = document.getElementById('faq_window')
        event.preventDefault();
        faqWindow.style.display = 'block';
       $.ajax({
           url: 'get_faq_data',
           type: 'GET',
           dataType: 'json',
           success: function (response){
               var data = response.data;
               var modalContent = $('#questions');
               modalContent.empty();
               for (var i = 0; i < data.length; i++){
                   modalContent.append('<h3 id="faq_q">' + data[i].question + '</h3>');
                   modalContent.append('<p id="faq_a">' + data[i].answer + '</p>');
               }
           }
    })}


 function applyFilters() {
     const selectedLevels = Array.from(document.getElementById('levelFilter').selectedOptions).map(option => option.value);
     const selectedDirections = Array.from(document.getElementById('directionFilter').selectedOptions).map(option => option.value);
     const selectedAvailabilities = Array.from(document.getElementById('availabilityFilter').selectedOptions).map(option => option.value);
     const selectedCosts = Array.from(document.getElementById('costFilter').selectedOptions).map(option => option.value);
     const selectedStudyTypes = Array.from(document.querySelectorAll('input[name="study-type"]:checked')).map(checkbox => checkbox.value);


     const urlParams = new URLSearchParams();
     if (selectedLevels.length > 0) {
    urlParams.append('level', selectedLevels.join(','));
  }
  if (selectedDirections.length > 0) {
    urlParams.append('direction', selectedDirections.join(','));
  }
  if (selectedAvailabilities.length > 0) {
    urlParams.append('availability', selectedAvailabilities.join(','));
  }
  if (selectedCosts.length > 0) {
    urlParams.append('cost', selectedCosts.join(','));
  }
  if (selectedStudyTypes.length > 0) {
    selectedStudyTypes.forEach(function (type) {
      urlParams.append('study-type', type);
    });
  }

  window.location.href = '/courses?' + urlParams.toString();
}

function getDataFromServer(studyId, isAnonymous) {
    const courseDetailsModal = document.getElementById('courseinfo');
    event.preventDefault();
    $.ajax({
        url: 'get_study',
        type: 'GET',
        dataType: 'json',
        data: { "study_id": studyId },
        success: function (response) {
            var data = response;
            console.log(data);
            var modalContent = $('#info');
            modalContent.empty();
            modalContent.append('<div class="description">'
                + '<div>'
                + '<div class="title">'
                + '<p>' + data.type + '</p>'
                + '<h3>' + data.title + '</h3>'
                + '</div>'
                + '<p>Рівень: ' + data.level + '</p>'
                + '<p>Тривалість: ' + data.time + '</p>'
                + '<p>Початок: ' + data.beginning + '</p>'
                + '</div>'
                + '<div class="image">' + '<img src="/static/' + data.image +'" alt="">'+'</div>'
                + '</div>'
                + '<p>Як проходить: ' + data.details + '</p>'
                + '<p>Кількість місць: ' + data.participants + '</p>'
                + '<p>Необхідне програмне забезпечення: ' + data.programs_settings + '</p>'
                + '<p>Ціна: ' + data.price + 'грн</p>'
                + '<input type="submit" onclick="seePaymentModal(' + data.id + ',' + isAnonymous + ')" value="Придбати" class="choose-course" >'
        );

        }
    });
    courseDetailsModal.style.display = 'block';
}

   const courseInfoModal = document.getElementById('courseinfo');
    var buyCourseId;
    const paymentModal = document.getElementById('buycourse');
    const confirmPaymentButton = document.getElementById('confirmPayment');
    const thankYouModal = document.getElementById('thankforbuying');
    const thankYouButton = document.getElementById('thanksButton');
    const buyErrorModal = document.getElementById('buyError');
    const logInSignUp = document.getElementById('loginsignup');

        function openPaymentModal() {
            paymentModal.style.display = 'block';
        }

        function closePaymentModal() {
            paymentModal.style.display = 'none';
        }

        function closeCourseInfoModal(){
            courseInfoModal.style.display = 'none';
        }

        function openThankYouModal() {
            thankYouModal.style.display = 'block';
        }

        function closeThankYouModal() {
            thankYouModal.style.display = 'none';
        }

        function openLogInSignUp(){
            logInSignUp.style.display = 'block';
        }

        function closeLogInSignUp(){
            logInSignUp.style.display = 'none';
        }

        function seePaymentModal(courseId, isAnonymous){
            if(isAnonymous){
                openLogInSignUp();
            }
            else {
                buyCourseId = courseId;
                closeCourseInfoModal();
                openPaymentModal();
            }
        }

        function openBuyErrorModal(){
            buyErrorModal.style.display = 'block';
        }

        function closeBuyErrorModal(){
            buyErrorModal.style.display = 'none';
        }

        confirmPaymentButton.addEventListener('click', function() {
             closePaymentModal();
            // openThankYouModal();
        });

        thankYouButton.addEventListener('click', function() {
             closeThankYouModal();
        });


        $('#payForm').submit(function(event){
             console.log('in function', buyCourseId)
            event.preventDefault();
            let formData = $(this).serialize();
            formData += '&courseId=' + buyCourseId;
            console.log('in function')
            $.ajax({
                type: 'POST',
                url: 'buy_course',
                data: formData,
                dataType: 'json'
            })
                .done(function (response){
                    if (response.success === true){
                        console.log('success')
                        openThankYouModal();
                    }else {
                        openPaymentModal();
                        openBuyErrorModal();
                        var modalContent = $('#new_content');
                        modalContent.empty();
                        console.log(response.errors)
                        for (var i = 0; i < response.errors.length; i++) {
                            modalContent.append('<h2 id="faq_q">' + response.errors[i] + '</h2>');
                        }
                    }
                });
            });
 $(document).ready(function() {
        $("[data-inputmask]").inputmask();
    });
String.prototype.toTitleCase = function () {
    return this.replace(/[\p{L}']+/gu, function (txt) {
        if (txt.charAt(0) === "'") {
            return "'" + txt.charAt(1).toLowerCase() + txt.substr(2).toLowerCase();
        } else {
            return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
        }
    });
};


function mask(target) {
    var elem = document.getElementById(target);
    elem.value = elem.value.replace(/[^a-zA-Zа-яА-ЯҐґЄєІіЇїЁё'\s-]/g, '').toTitleCase().replace(/\s+/g, ' ');
}