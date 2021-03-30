(function ($) {
    "use strict";
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
//     /*==================================================================[ Validate ]*/

   

 

//     // Upload Quickbook file
    $('#btn').click(function(e){
        e.preventDefault();
        // console.log("click");
        var this_context = $(this);
        var csrftoken = getCookie('csrftoken');
        if($('#dhaka').prop('checked')) {
            var dhaka='dhaka';
        } else {
            dhaka=null;
        }
        if($('#dinajpur').prop('checked')) {
            var dinajpur='dinajpur';
        } else {
            dinajpur=null;
        }
        if($('#rajshahi').prop('checked')) {
            var rajshahi='rajshahi';
        } else {
            rajshahi=null;
        }
        ///////////////////////////////////////////////////////
        if($('#sujon').prop('checked')) {
            var sujon='sujon';
        } else {
            sujon=null;
        }
        if($('#kamal').prop('checked')) {
            var kamal='kamal';
        } else {
            kamal=null;
        }
        if($('#monir').prop('checked')) {
            var monir='monir';
        } else {
            monir=null;
        }
 //////////////////////////////////////////////////////
        if($('#yesterday').prop('checked')) {
            var yesterday=1;
        } else {
            yesterday=0;
        }
        if($('#lastweek').prop('checked')) {
            var lastweek=1;
        } else {
            lastweek=0;
        }
        if($('#lastmonth').prop('checked')) {
            var lastmonth=1;
        } else {
            lastmonth=0;
        }
////////////////////////////////////////////
        var startdate= $('input[name=startDate]').val();
        var enddate = $('input[name=endDate]').val();
///////////////////////////////////////////
        if($('#pass').prop('checked')) {
            var pass=1;
        } else {
            pass=0;
        }
        if($('#fail').prop('checked')) {
            var fail=1;
        } else {
            fail=0;
        }
        // console.log(startdate);
        // console.log(enddate);
        var formData={"dhaka":dhaka,"dinajpur":dinajpur,"rajshahi":rajshahi,"sujon":sujon,"kamal":kamal,"monir":monir,"yesterday":yesterday,"lastweek":lastweek,"lastmonth":lastmonth, "startdate":startdate, "enddate":enddate,"pass":pass,"fail":fail,csrfmiddlewaretoken:csrftoken};
        $.ajax({
            url: '',
            type: 'POST',
            data: formData,
            // enctype: 'multipart/form-data',
            // contentType: false,
            // processData: false,
            headers: {
                'X-CSRFToken': csrftoken 
            },
            beforeSend: function(){
                this_context.addClass('d-none');
                // this_context.parent().find('.loader').removeClass('d-none');
            },
            success: function (response) {
                // console.log(response);
                
                // console.log(response[0].id);
                // console.log(response[0].name);
                var html='<table class="table table-dark"><thead><tr><th scope="col">Roll</th><th scope="col">Name</th><th scope="col">City</th><th scope="col">Marks</th><th scope="col">Status</th><th scope="col">Created</th></tr></thead><tbody>';
                response.forEach(function (arrayItem) {
                    // console.log(arrayItem.Head_of_the_Household_s_Name);
                    // console.log("-----------");
                //    console.log(arrayItem.marks);
                   html+="<tr scope='row'>";
                       html+= "<td>"+ arrayItem.roll+"</td>"+"<td>"+ arrayItem.name+"</td>"+"<td>"+ arrayItem.city+"</td>"+"<td>"+  arrayItem.marks+"</td>"+"<td>"+  arrayItem.pass_fail+"</td>"+"<td>"+  arrayItem.created+"</td>"
                   html+="</tr>"
                });
                html+='</tbody></table>';
                $('#tbl1').html(html);
                // var mydata=JSON.parse(response)
                // console.log(mydata)

                // toastr.success('File Upload successful');
                // localStorage.setItem("quick_book", response.data.filename);
            },
            error: function(err) {
                // console.log(err);
                // toastr.error('uploaded file not valid')
            },
            complete: function(res, err){
                // this_context.parent().find('.loader').addClass('d-none');
                this_context.removeClass('d-none');
            }
        });
    });

   

})(jQuery);
