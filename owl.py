# #!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
# print("content-type:text/html \r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.min.css" integrity="sha512-tS3S5qG0BlhnQROyJXvNjeEM4UpMXHrQfTGmbQ1gKmelCxlSEBUaxhRBj/EFTzpbP4RVSrpEikbmdJobCvhE3g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.theme.default.min.css" integrity="sha512-sMXtMNL1zRzolHYKEujM2AqCLUR9F2C4/05cdbxjjLSRvMQIciEPCQZo++nk7go3BtSuK9kfa/s+a4f4i5pLkw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>

   <div class="container-fluid">
        <div class="owl--container">
            <div class="row">
                <div class="col-md-12">
                    <h4 class="jumbotron fs-3">Trendy Fashion Wears</h4>
                </div><br><br>
                <div class="col-md-12">
                    <div class="owl-carousel owl-theme">
                        <div class="item">
                            <img src="assets/womenblk.jpg" alt="">
                        </div>
                        <div class="item">
                            <img src="assets/mencat.jpg" alt="">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div><br><br><br>

    <div class="container-fluid">
        <div class="owl--container">
            <div class="row">
                <div class="col-md-12">
                    <h4 class="jumbotron fs-3 text-capitalize">Appliances for you home</h4>
                </div><br><br>
                <div class="col-md-12">
                    <div class="owl-carousel owl-theme">
                        <div class="item">
                            <img src="assets/homecat.jpg" alt="">
                        </div>
                        <div class="item">
                            <img src="assets/homecat.jpg" alt="">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div><br><br><br>

    <div class="container-fluid">
        <div class="owl--container">
            <div class="row">
                <div class="col-md-12">
                    <h4 class="jumbotron fs-3 text-capitalize">Smart Electronics</h4>
                </div><br><br>
                <div class="col-md-12">
                    <div class="owl-carousel owl-theme">
                        <div class="item">
                           <a href="#"> <img src="assets/eleccat.jpg" alt=""></a>
                        </div>
                        <!-- <div class="item">
                            <img src="/assets/eleccat" alt="">
                        </div> -->
                    </div>
                </div>
            </div>
        </div>
    </div><br><br><br>
    
     <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/owl.carousel.min.js" integrity="sha512-bPs7Ae6pVvhOSiIcyUClR7/q2OAsRiovw4vAkX+zJbw3ShAeeqezq50RIIcIURq7Oa20rW2n2q+fyXBNcU9lrw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    
    <script>
        
        $(document).ready(function(){
            $('.owl-carousel').owlCarousel({
                loop:true,
                margin:10,
                nav:true,
                autowidth: true,
                autoheight: true,
                autoplay:true,
                autoplayTimeout:1200,
                stagePadding: 50,
                responsive:{
                    0:{
                        items:1
                    },
                    600:{
                        items:3
                    },
                    1000:{
                        items:5
                    }
                }
            });
        });

    </script>

   

</body>
</html>

""")