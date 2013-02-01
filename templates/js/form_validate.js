jQuery(document).ready(function () {
    jQuery("#sign_up_form").validationEngine('attach', {
        focusFirstField:true,
        showOneMessage:true,
        scroll:false,
        promptPosition:"topRight",
        custom_error_messages:{
            autoHidePrompt: true,
            '#id_username':{
                'required':{'message': "Please enter username"}
            },

            '#id_email':{
                'required':{'message': "Please enter email"}
            },

            '#id_password1':{
                'required':{'message': "Please enter password"}
            },

            '#id_day_dob':{
                'required':{'message': "Please enter your birth day"}
            },

            '#id_month_dob':{
                'required':{'message': "Please enter your birth day"}
            },

            '#id_year_dob':{
                'required':{'message': "Please enter your birth day"}
            },

            '#id_first_name':{
                'required':{'message': "Please enter your first name"}
            },

            '#id_last_name':{
                'required':{'message': "Please enter your last name"}
            }
        }
    });
});