$(document).ready(function(){
    $('.item').hide();
    $('.basket-detail').slideUp();
    $('.order-detail').slideUp();
    
	var totalPosition = $('.total');
    totalPosition.data('total', 0);
    var amountPosition = $('#amount');

    $('.item').each(function(){
    	$(this).data( 'clothType', $(this).find('td').first().text() );
    	$(this).data('unitPrice', parseInt($(this).children('td').eq(1).text()) );
    });

	var buildingPosition = $('.buildings');

	$('#basket-button').on('click', function(){
		$(document).find('.item-list').slideToggle();
		$(document).find('.basket-detail').slideToggle();
	});

	$('.product').on('click', function(){
		var num = Number(amountPosition.text());
		amountPosition.text(num+1);
		var clothType = $(this).attr('id').substring(8);
		var str1 = ".item-";
		var itemClass = str1.concat(clothType);
		var position = $(itemClass);
		num = Number(position.find('span').text());
		position.find('span').text(num+1);
		position.show();
		totalPosition.text(Number(totalPosition.text())+Number(position.children('td').eq(1).text()));
	});

	$('.count-add').on('click', function(){
		var count = $(this).next();
		var num = Number(count.text());
		count.text(num+1);
		amountPosition.text(Number(amountPosition.text())+1);
		totalPosition.text(Number(totalPosition.text())+Number(count.parent().prev().text()));
	});

	$('.count-minus').on('click', function(){
		var count = $(this).prev();
		var num = Number(count.text());
		amountPosition.text(Number(amountPosition.text()-1));
		count.text(num-1);
		totalPosition.text(Number(totalPosition.text())-Number(count.parent().prev().text()));
		if (num == 1)
			count.parent().parent().hide();
		else
			count.text(num-1);
	});

	$('#basket-ok').on('click', function(){
		if ( Number(amountPosition.text()) == 0)
		{
			alert("You haven't select any cloth yet.");
		}
		else
		{
			$(".basket-detail").slideToggle();
			$(".order-detail").slideToggle();
		}
	});

	$('#basket-back').on('click', function(){
		$('.basket-detail').slideToggle();
		$('.item-list').slideToggle();
	});

	$('#order').on('click', function(){
		var itemlist = [];
		$('.item').each(function(){
			var type = $(this).data('clothType');
    		var unitPrice = parseInt($(this).data('unitPrice'));
    		var quantity = parseInt($(this).find('span').text());
    		itemlist.push( { type: type, unitPrice: unitPrice, quantity: quantity} );
		});

		var data = {
			memo: $('#memo').val(),
			customerId: 123,
			sumPrice: parseInt(totalPosition.text()),
			addrId: parseInt($(".addr").val()),
			itemlist: itemlist,
		};
		console.log(data);

		var csrftoken = $.cookie('csrftoken');
		function csrfSafeMethod(method) {
		    // these HTTP methods do not require CSRF protection
		    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
		$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});
		
		$.ajax({
			type: 'POST',
			url: '/makeOrder/',
			data: JSON.stringify(data),
			success: function( msg ){
				alert(msg);
				window.location.replace("http://127.0.0.1:8000");
			},
			error: function(){
				alert(err);
			},
		});
	});
	
});