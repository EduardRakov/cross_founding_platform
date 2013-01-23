$.validator.setDefaults({
    submitHandler:function () {
        document.forms.submit()
    }
});

$(document).ready(function() {

    $("#studentForm").validate({

        rules: {

            first_name: {
                text_field: true,
                minlength: 2,
                maxlength: 20,
                required: true
            },

            last_name: {
                text_field: true,
                minlength: 2,
                maxlength: 20,
                required: true
            },

            password: {
                minlength: 6,
                maxlength: 20,
                required: true
            },

            e_mail: {
                required: true,
                email: true
            },

            phone: {
                minlength: 5,
                maxlength: 10,
                digits: true,
                required: true
            },

            find_about_us: {
                required: true
            },

            agree: {
                required: true
            }

        }
    });
});