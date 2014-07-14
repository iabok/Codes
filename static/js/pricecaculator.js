/**
 * Created by isaac on 7/11/14.
 */

$        $(function() {
            $(".inline.{{ use_form.prefix }}").formset({
                prefix: "{{ use_form.prefix }}",
                animateForms: true,
                fadeIn:true

            });


            $(".inline.{{ placement_form.prefix }}").formset({
                prefix: "{{ placement_form.prefix }}",
                animateForms: true,
                fadeIn:true

            });

            $(".inline.{{ size_form.prefix }}").formset({
                prefix: "{{ size_form.prefix }}",
                animateForms: true,
                fadeIn:true

            });

            $(".inline.{{ territory_form.prefix }}").formset({
                prefix: "{{ territory_form.prefix }}",
                animateForms: true,
                fadeIn:true

            });

            $(".inline.{{ duration_form.prefix }}").formset({
                prefix: "{{ duration_form.prefix }}",
                animateForms: true,
                fadeIn:true

            });

            $(".inline.{{ print_run_form.prefix }}").formset({
                prefix: "{{ duration_form.prefix }}",
                animateForms: true,
                fadeIn:true

            });
        });

      $(document).ready(function(){

          $(this).find('.inline').each(function() {
              $(this).hide();
              $('.btn-primary').hide();
              $('#show').hide();
          });

          $("#price-show").mouseover(function(){
             $(this).find('#show').each(function() {
	         $(this).fadeIn();
             $('#show').click(function(){
                    $(this).find('.inline ').each(function() {
                    $(this).fadeIn();
                    $('btn-primary').show();
                  });
                 });
             });
          }).mouseout(function(){
             $(this).find('#price-show').each(function() {
                  $(this).hide();

              });
          });



    });
