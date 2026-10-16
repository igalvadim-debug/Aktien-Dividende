<!DOCTYPE html>
<!-- saved from url=(0082)https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server -->
<html lang="de" dir="ltr" prefix="og: https://ogp.me/ns#" class=" js"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
<noscript><style>form.antibot > * { display: none !important; } form.antibot noscript { display: block !important; }</style>
</noscript><meta name="description" content="Sie möchten OpenCloud produktiv betreiben – mit eigener Domain, gültigen TLS-Zertifikaten und Weboffice? In diesem Artikel erfahren Sie Schritt für Schritt, wie Sie OpenCloud auf einem bestehenden Server einrichten und nahtlos in Ihre Infrastruktur integrieren.">
<meta name="keywords" content="OpenCloud, Open Source, Installationsanleitung">
<link rel="canonical" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server">
<meta name="robots" content="index, follow">
<meta property="og:title" content="OpenCloud installieren – ganz einfach auf dem eigenen Server">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="OpenCloud installieren – ganz einfach auf dem eigenen Server | OpenCloud">
<meta name="google-site-verification" content="JP-aRzNcGVOXzcEqKJOUVYfZ0KrW-6RK2lZci15P4EU">
<meta name="Generator" content="Drupal 11 (https://www.drupal.org); Commerce 3">
<meta name="MobileOptimized" content="width">
<meta name="HandheldFriendly" content="true">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="alternate" hreflang="de" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server">
<link rel="alternate" hreflang="en" href="https://opencloud.eu/en/install-opencloud-simply-your-own-server">

    <title>OpenCloud installieren – ganz einfach auf dem eigenen Server | OpenCloud</title>
    <meta name="format-detection" content="telephone=no">
    <link rel="stylesheet" media="all" href="./opencloud_files/8628052440e532f890cfc00d4a682fa6.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/018b84b545f1b1c2d79f7133f25b94d5.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/bb97af618e143d699c9b1490259df7a2.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/da4ff6b7023d551cabc779c4ecd2514b.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/ac3a25c1a721ff659377d3b401a42f7d.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/e382578eb43cf75a084cec3d99e569b4.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/83e68dbaa6a9f95f657ec1759b8baabd.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/cd068c6fabd914c8903962e639ebecc3.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/6bf7857dc423eada40ddf4aec0506587.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/8ed3f14dc4200f10cbcc1279747bbe39.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/cfd869694de3e66f4725d0956056988f.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/a77c6ab7742585fc8266a5f41b392699.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/ccb5591b3a19d789a248e75fc4ece74f.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/dfda5a5a86af7c6beecc68f0a6d08746.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/5337f6782c333ee3190e9916d1d55945.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/f35450605bdf0bee93116139f5d55894.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/896397d7244d968ab59870c04eaf5a7f.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/aae05a69c245675a178190f88dedcc80.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/3e350199a1234c38c350d0e0b745854f.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/6a9f82db0544249bb4705bc6d8225d49.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/c01c446d9be3479da635580245cc6074.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/a16f52878f1bbc20fdb40221ab2cbef0.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/dc79bb759d046d4096b8e5372702b13d.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/e1f7ab429cddee3fecb9b6e737934741.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/8d27243922b47430224334c6e1eb8778.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/2035508b02955b46e32b798f0650f0c4.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/7209d68409ad265a9362dd9a4f121185.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/af93bb2070fe9014644c2dc51adeffe6.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/e22a7eb3794133e35a6134ee33e06a3d.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/b1c744b86376885f21081c9e97b3113c.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/0bc7570a128b32be9381159d37b2e84d.min.css">
<link rel="stylesheet" media="all" href="./opencloud_files/ff56b7b15b68a59722e867af540cc14f.min.css">

    

    <link rel="apple-touch-icon" sizes="180x180" href="https://opencloud.eu/themes/cloudy/src/assets/favicon/web-app-manifest-192x192.png">
    <link rel="apple-touch-icon" sizes="180x180" href="https://opencloud.eu/themes/cloudy/src/assets/favicon/web-app-manifest-512x512.png">
    <link rel="icon" type="image/png" href="https://opencloud.eu/themes/cloudy/src/assets/favicon/favicon-96x96.png" sizes="96x96">
    <link rel="icon" type="image/svg+xml" href="https://opencloud.eu/themes/cloudy/src/assets/favicon/favicon.svg">
    <link rel="shortcut icon" href="https://opencloud.eu/themes/cloudy/src/assets/favicon/favicon.svg" type="image/svg+xml">
    <link rel="manifest" href="https://opencloud.eu/themes/cloudy/src/assets/favicon/site.webmanifest">

    <meta name="theme-color" content="#ffffff">

            <script async="" src="./opencloud_files/container_U8PmBgOA.js.Download"></script><script src="./opencloud_files/matomo-head.js.Download"></script>
      </head>
  <body>
        <a href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server#main-content" class="visually-hidden focusable">
      Direkt zum Inhalt
    </a>
    
      <div class="dialog-off-canvas-main-canvas" data-off-canvas-main-canvas="">
    

<div class="sheet sheet--headarea-shy">

  <div class="sheet__header">
    


<div class="headarea headarea--content_hub headarea--init headarea--inited headarea--motion headarea--shy">
  <div class="headarea__shy-wrapper">
    <div class="headarea__row">
      <div class="headarea__col">
        <div class="headarea__logo">
          


<a href="https://opencloud.eu/de" class="logo ">
      <svg class="logo__svg" xmlns="http://www.w3.org/2000/svg" width="195" height="43" viewBox="0 0 847.73 179.09"><path d="M226.76,120.48c-12.96-7.31-20.51-20.74-20.51-37.59,0-8.48,1.77-16.03,5.42-22.63,7.07-13.2,20.51-20.98,37.36-20.98,8.37,0,15.67,1.89,22.16,5.54,12.85,7.42,20.27,21.09,20.27,38.06,0,8.37-1.77,15.91-5.3,22.39-7.07,13.08-20.51,20.74-37.12,20.74-8.37,0-15.79-1.77-22.27-5.54ZM248.92,112.46c16.5,0,27.34-11.55,27.34-29.58s-11.43-30.17-27.34-30.17-27.46,11.67-27.46,30.17,10.96,29.58,27.46,29.58Z" fill="#20434f"></path><path d="M310.48,62.26l7.78,13.67c7.07-11.2,16.38-13.67,23.57-13.67,5.77,0,10.72,1.3,15.08,4.12,4.48,2.95,7.9,6.72,10.14,11.43,2.47,4.95,3.65,10.37,3.65,16.38s-1.18,11.55-3.65,16.5c-2.24,4.71-5.78,8.49-10.25,11.2-4.24,2.83-9.19,4.12-14.97,4.12-3.89,0-7.78-.82-11.55-2.47-3.42-1.65-6.48-4.01-8.96-6.95v29.93h-14.38v-61.63l-8.84-15.44,12.37-7.19ZM321.33,94.2c0,3.65.71,7.07,2.12,10.02,1.77,3.18,3.77,5.42,6.13,6.84,2.71,1.53,5.66,2.24,9.07,2.24s6.48-.71,9.07-2.24c2.59-1.53,4.71-3.77,6.01-6.84,1.53-2.95,2.12-6.36,2.12-10.02,0-5.89-1.53-10.6-4.59-13.91-3.18-3.53-7.31-5.3-12.73-5.3-5.07,0-9.31,1.77-12.49,5.3-3.06,3.3-4.71,8.01-4.71,13.91Z" fill="#20434f"></path><path d="M382.08,77.82c2.36-4.71,5.89-8.6,10.72-11.67,4.95-2.71,10.37-4.01,16.62-4.01s11.43,1.3,15.56,3.77c4.48,2.83,7.78,6.6,10.14,11.31,2.12,4.83,3.3,10.61,3.3,16.97l-.23,3.42h-45.84c.47,5.3,2.36,9.31,5.66,12.37,3.3,2.59,7.66,3.77,12.85,3.77,4.01,0,7.54-.71,10.84-2,3.3-1.3,6.25-2.95,8.6-4.95.35.35,6.13,10.49,6.13,10.49-3.65,2.71-7.78,4.83-12.26,6.48-4.12,1.53-8.96,2.24-14.26,2.24-6.36,0-12.02-1.3-16.62-4.01-4.48-2.59-8.13-6.36-11.08-11.31-2.59-4.95-3.89-10.49-3.89-16.5s1.18-11.43,3.77-16.38ZM392.69,87.83h31.46c-.47-4.71-2-8.01-4.6-10.13-2.83-2.47-6.13-3.77-10.13-3.77s-7.66,1.3-10.84,3.54c-2.83,2.24-4.71,5.66-5.89,10.37Z" fill="#20434f"></path><path d="M508.5,87.36v36.77h-14.49v-35.47c0-4.83-1.06-8.25-3.3-10.49-2.12-2.59-5.3-3.77-9.66-3.77-2.83,0-5.19.71-7.54,2.24-2.24,1.18-4.01,3.18-5.19,5.66-1.06,2.36-1.77,5.19-1.77,8.6v33.23h-14.61v-39.24l-8.84-15.56,12.49-7.07,7.31,12.49c7.42-11.08,15.44-12.49,20.86-12.49,6.13,0,9.9,1.06,12.37,2.24,2.47,1.18,4.71,2.71,6.36,4.6,4.01,4.36,6.01,10.49,6.01,18.27Z" fill="#20434f"></path><path d="M585.22,120.95c-2.59,1.3-6.01,2.59-10.25,3.77-3.89.83-8.01,1.3-12.37,1.3-8.49,0-16.03-1.88-22.51-5.42-6.36-3.54-11.31-8.6-14.97-15.32-3.54-6.48-5.3-14.02-5.3-22.63s1.77-15.91,5.19-22.63c3.42-6.6,8.72-11.78,14.97-15.2,6.48-3.77,14.26-5.54,23.45-5.54,4.6,0,8.6.35,12.02,1.3,4.01.94,7.31,2.12,9.66,3.53,2.48,1.18,5.42,2.83,8.84,5.07l-7.43,12.61c-3.65-2.47-7.19-4.36-10.61-5.77-4.01-1.53-8.25-2.36-12.85-2.36-6.13,0-11.2,1.18-15.2,3.65-4.36,2.71-7.54,6.13-9.66,10.37-2.12,4.6-3.3,9.66-3.3,15.2s1.18,10.49,3.3,14.85c2.12,4.24,5.3,7.66,9.66,10.14,4.12,2.36,9.19,3.53,15.08,3.53,3.42,0,6.48-.35,9.31-1.06,3.06-.83,5.66-1.77,7.78-2.95,2.95-1.53,5.19-2.95,6.84-4.24l7.31,12.73c-3.53,2.12-6.48,3.89-8.96,5.07Z" fill="#20434f"></path><path d="M603,124.13V38.69h14.38v85.44h-14.38Z" fill="#20434f"></path><path d="M628.11,94.2c0-18.62,13.2-31.94,32.17-31.94s31.94,13.2,31.94,31.82-13.08,31.94-32.06,31.94-32.05-12.37-32.05-31.82ZM660.17,113.64c10.14,0,17.09-7.19,17.09-19.56s-6.95-19.56-17.09-19.56-17.21,7.9-17.21,19.56,6.84,19.56,17.21,19.56Z" fill="#20434f"></path><path d="M725.55,126.02c-6.95,0-12.49-2.12-16.73-6.72-4.01-4.59-6.01-10.84-6.01-18.62v-36.53h14.38v35.47c0,4.6,1.06,8.13,3.3,10.61,2.12,2.36,5.42,3.42,9.78,3.42,2.83,0,5.3-.59,7.54-1.89,2.24-1.3,3.89-3.3,5.07-5.77,1.3-2.59,1.88-5.54,1.88-8.6v-33.23h14.5v39.6l8.72,15.2-12.37,7.07-6.95-11.9s-2.71,3.54-6.36,6.6c-4.48,3.77-9.19,5.3-16.73,5.3Z" fill="#20434f"></path><path d="M776.31,77.82c2.71-5.3,5.89-9.19,10.25-11.43,4.36-2.71,9.43-4.24,14.85-4.24,4.6,0,8.37.94,11.67,2.59,3.3,1.65,6.36,3.77,8.84,6.95v-33h14.38v64.93l8.6,15.2-12.37,7.07-7.54-13.08s-5.19,7.31-11.9,10.61c-2.83,1.41-7.31,2.48-11.55,2.48-5.54,0-10.61-1.3-14.97-4.13-4.24-2.24-7.54-6.13-10.25-11.08-2.48-4.95-3.53-10.25-3.53-16.5s1.06-11.78,3.53-16.38ZM787.5,94.2c0,4.01.71,7.19,2.12,9.9,1.65,3.3,3.77,5.3,6.01,6.72,2.59,1.53,5.42,2.36,8.96,2.36s6.6-.83,9.07-2.36c2.47-1.41,4.59-3.54,6.13-6.72,1.42-2.71,2.12-5.89,2.12-9.9,0-5.89-1.53-10.84-4.83-13.91-2.83-3.53-7.19-5.42-12.37-5.42s-9.43,1.89-12.37,5.42c-3.3,3.06-4.83,8.01-4.83,13.91Z" fill="#20434f"></path><polygon points="69.63 129.25 76.91 125.05 76.91 94.64 103.09 79.52 103.09 71.14 95.81 66.94 69.46 82.15 43.47 67.15 36.19 71.35 36.19 79.73 62.37 94.85 62.37 125.06 69.63 129.25" fill="#20434f"></polygon><polygon points="136.44 41.4 69.64 2.83 69.64 2.84 69.64 2.83 2.83 41.4 2.83 58.19 69.64 19.62 136.44 58.19 136.44 41.4" fill="#20434f"></polygon><polygon points="136.44 120.9 69.64 159.47 2.84 120.9 2.84 137.69 69.64 176.26 69.64 176.25 69.64 176.26 136.44 137.69 136.44 120.9" fill="#20434f"></polygon></svg>
  
      <svg class="logo__mobile" xmlns="http://www.w3.org/2000/svg" width="200" height="45" viewBox="0 0 847.73 179.09"><path d="M226.76,120.48c-12.96-7.31-20.51-20.74-20.51-37.59,0-8.48,1.77-16.03,5.42-22.63,7.07-13.2,20.51-20.98,37.36-20.98,8.37,0,15.67,1.89,22.16,5.54,12.85,7.42,20.27,21.09,20.27,38.06,0,8.37-1.77,15.91-5.3,22.39-7.07,13.08-20.51,20.74-37.12,20.74-8.37,0-15.79-1.77-22.27-5.54ZM248.92,112.46c16.5,0,27.34-11.55,27.34-29.58s-11.43-30.17-27.34-30.17-27.46,11.67-27.46,30.17,10.96,29.58,27.46,29.58Z" fill="#20434f"></path><path d="M310.48,62.26l7.78,13.67c7.07-11.2,16.38-13.67,23.57-13.67,5.77,0,10.72,1.3,15.08,4.12,4.48,2.95,7.9,6.72,10.14,11.43,2.47,4.95,3.65,10.37,3.65,16.38s-1.18,11.55-3.65,16.5c-2.24,4.71-5.78,8.49-10.25,11.2-4.24,2.83-9.19,4.12-14.97,4.12-3.89,0-7.78-.82-11.55-2.47-3.42-1.65-6.48-4.01-8.96-6.95v29.93h-14.38v-61.63l-8.84-15.44,12.37-7.19ZM321.33,94.2c0,3.65.71,7.07,2.12,10.02,1.77,3.18,3.77,5.42,6.13,6.84,2.71,1.53,5.66,2.24,9.07,2.24s6.48-.71,9.07-2.24c2.59-1.53,4.71-3.77,6.01-6.84,1.53-2.95,2.12-6.36,2.12-10.02,0-5.89-1.53-10.6-4.59-13.91-3.18-3.53-7.31-5.3-12.73-5.3-5.07,0-9.31,1.77-12.49,5.3-3.06,3.3-4.71,8.01-4.71,13.91Z" fill="#20434f"></path><path d="M382.08,77.82c2.36-4.71,5.89-8.6,10.72-11.67,4.95-2.71,10.37-4.01,16.62-4.01s11.43,1.3,15.56,3.77c4.48,2.83,7.78,6.6,10.14,11.31,2.12,4.83,3.3,10.61,3.3,16.97l-.23,3.42h-45.84c.47,5.3,2.36,9.31,5.66,12.37,3.3,2.59,7.66,3.77,12.85,3.77,4.01,0,7.54-.71,10.84-2,3.3-1.3,6.25-2.95,8.6-4.95.35.35,6.13,10.49,6.13,10.49-3.65,2.71-7.78,4.83-12.26,6.48-4.12,1.53-8.96,2.24-14.26,2.24-6.36,0-12.02-1.3-16.62-4.01-4.48-2.59-8.13-6.36-11.08-11.31-2.59-4.95-3.89-10.49-3.89-16.5s1.18-11.43,3.77-16.38ZM392.69,87.83h31.46c-.47-4.71-2-8.01-4.6-10.13-2.83-2.47-6.13-3.77-10.13-3.77s-7.66,1.3-10.84,3.54c-2.83,2.24-4.71,5.66-5.89,10.37Z" fill="#20434f"></path><path d="M508.5,87.36v36.77h-14.49v-35.47c0-4.83-1.06-8.25-3.3-10.49-2.12-2.59-5.3-3.77-9.66-3.77-2.83,0-5.19.71-7.54,2.24-2.24,1.18-4.01,3.18-5.19,5.66-1.06,2.36-1.77,5.19-1.77,8.6v33.23h-14.61v-39.24l-8.84-15.56,12.49-7.07,7.31,12.49c7.42-11.08,15.44-12.49,20.86-12.49,6.13,0,9.9,1.06,12.37,2.24,2.47,1.18,4.71,2.71,6.36,4.6,4.01,4.36,6.01,10.49,6.01,18.27Z" fill="#20434f"></path><path d="M585.22,120.95c-2.59,1.3-6.01,2.59-10.25,3.77-3.89.83-8.01,1.3-12.37,1.3-8.49,0-16.03-1.88-22.51-5.42-6.36-3.54-11.31-8.6-14.97-15.32-3.54-6.48-5.3-14.02-5.3-22.63s1.77-15.91,5.19-22.63c3.42-6.6,8.72-11.78,14.97-15.2,6.48-3.77,14.26-5.54,23.45-5.54,4.6,0,8.6.35,12.02,1.3,4.01.94,7.31,2.12,9.66,3.53,2.48,1.18,5.42,2.83,8.84,5.07l-7.43,12.61c-3.65-2.47-7.19-4.36-10.61-5.77-4.01-1.53-8.25-2.36-12.85-2.36-6.13,0-11.2,1.18-15.2,3.65-4.36,2.71-7.54,6.13-9.66,10.37-2.12,4.6-3.3,9.66-3.3,15.2s1.18,10.49,3.3,14.85c2.12,4.24,5.3,7.66,9.66,10.14,4.12,2.36,9.19,3.53,15.08,3.53,3.42,0,6.48-.35,9.31-1.06,3.06-.83,5.66-1.77,7.78-2.95,2.95-1.53,5.19-2.95,6.84-4.24l7.31,12.73c-3.53,2.12-6.48,3.89-8.96,5.07Z" fill="#20434f"></path><path d="M603,124.13V38.69h14.38v85.44h-14.38Z" fill="#20434f"></path><path d="M628.11,94.2c0-18.62,13.2-31.94,32.17-31.94s31.94,13.2,31.94,31.82-13.08,31.94-32.06,31.94-32.05-12.37-32.05-31.82ZM660.17,113.64c10.14,0,17.09-7.19,17.09-19.56s-6.95-19.56-17.09-19.56-17.21,7.9-17.21,19.56,6.84,19.56,17.21,19.56Z" fill="#20434f"></path><path d="M725.55,126.02c-6.95,0-12.49-2.12-16.73-6.72-4.01-4.59-6.01-10.84-6.01-18.62v-36.53h14.38v35.47c0,4.6,1.06,8.13,3.3,10.61,2.12,2.36,5.42,3.42,9.78,3.42,2.83,0,5.3-.59,7.54-1.89,2.24-1.3,3.89-3.3,5.07-5.77,1.3-2.59,1.88-5.54,1.88-8.6v-33.23h14.5v39.6l8.72,15.2-12.37,7.07-6.95-11.9s-2.71,3.54-6.36,6.6c-4.48,3.77-9.19,5.3-16.73,5.3Z" fill="#20434f"></path><path d="M776.31,77.82c2.71-5.3,5.89-9.19,10.25-11.43,4.36-2.71,9.43-4.24,14.85-4.24,4.6,0,8.37.94,11.67,2.59,3.3,1.65,6.36,3.77,8.84,6.95v-33h14.38v64.93l8.6,15.2-12.37,7.07-7.54-13.08s-5.19,7.31-11.9,10.61c-2.83,1.41-7.31,2.48-11.55,2.48-5.54,0-10.61-1.3-14.97-4.13-4.24-2.24-7.54-6.13-10.25-11.08-2.48-4.95-3.53-10.25-3.53-16.5s1.06-11.78,3.53-16.38ZM787.5,94.2c0,4.01.71,7.19,2.12,9.9,1.65,3.3,3.77,5.3,6.01,6.72,2.59,1.53,5.42,2.36,8.96,2.36s6.6-.83,9.07-2.36c2.47-1.41,4.59-3.54,6.13-6.72,1.42-2.71,2.12-5.89,2.12-9.9,0-5.89-1.53-10.84-4.83-13.91-2.83-3.53-7.19-5.42-12.37-5.42s-9.43,1.89-12.37,5.42c-3.3,3.06-4.83,8.01-4.83,13.91Z" fill="#20434f"></path><polygon points="69.63 129.25 76.91 125.05 76.91 94.64 103.09 79.52 103.09 71.14 95.81 66.94 69.46 82.15 43.47 67.15 36.19 71.35 36.19 79.73 62.37 94.85 62.37 125.06 69.63 129.25" fill="#20434f"></polygon><polygon points="136.44 41.4 69.64 2.83 69.64 2.84 69.64 2.83 2.83 41.4 2.83 58.19 69.64 19.62 136.44 58.19 136.44 41.4" fill="#20434f"></polygon><polygon points="136.44 120.9 69.64 159.47 2.84 120.9 2.84 137.69 69.64 176.26 69.64 176.25 69.64 176.26 136.44 137.69 136.44 120.9" fill="#20434f"></polygon></svg>
  </a>
        </div>
        <div class="headarea__logo headarea__logo-hover">
          


<a href="https://opencloud.eu/de" class="logo ">
      <svg class="logo__svg" xmlns="http://www.w3.org/2000/svg" width="195" height="43" viewBox="0 0 847.73 179.09"><path d="M226.76,120.48c-12.96-7.31-20.51-20.74-20.51-37.59,0-8.48,1.77-16.03,5.42-22.63,7.07-13.2,20.51-20.98,37.36-20.98,8.37,0,15.67,1.89,22.16,5.54,12.85,7.42,20.27,21.09,20.27,38.06,0,8.37-1.77,15.91-5.3,22.39-7.07,13.08-20.51,20.74-37.12,20.74-8.37,0-15.79-1.77-22.27-5.54ZM248.92,112.46c16.5,0,27.34-11.55,27.34-29.58s-11.43-30.17-27.34-30.17-27.46,11.67-27.46,30.17,10.96,29.58,27.46,29.58Z" fill="#20434f"></path><path d="M310.48,62.26l7.78,13.67c7.07-11.2,16.38-13.67,23.57-13.67,5.77,0,10.72,1.3,15.08,4.12,4.48,2.95,7.9,6.72,10.14,11.43,2.47,4.95,3.65,10.37,3.65,16.38s-1.18,11.55-3.65,16.5c-2.24,4.71-5.78,8.49-10.25,11.2-4.24,2.83-9.19,4.12-14.97,4.12-3.89,0-7.78-.82-11.55-2.47-3.42-1.65-6.48-4.01-8.96-6.95v29.93h-14.38v-61.63l-8.84-15.44,12.37-7.19ZM321.33,94.2c0,3.65.71,7.07,2.12,10.02,1.77,3.18,3.77,5.42,6.13,6.84,2.71,1.53,5.66,2.24,9.07,2.24s6.48-.71,9.07-2.24c2.59-1.53,4.71-3.77,6.01-6.84,1.53-2.95,2.12-6.36,2.12-10.02,0-5.89-1.53-10.6-4.59-13.91-3.18-3.53-7.31-5.3-12.73-5.3-5.07,0-9.31,1.77-12.49,5.3-3.06,3.3-4.71,8.01-4.71,13.91Z" fill="#20434f"></path><path d="M382.08,77.82c2.36-4.71,5.89-8.6,10.72-11.67,4.95-2.71,10.37-4.01,16.62-4.01s11.43,1.3,15.56,3.77c4.48,2.83,7.78,6.6,10.14,11.31,2.12,4.83,3.3,10.61,3.3,16.97l-.23,3.42h-45.84c.47,5.3,2.36,9.31,5.66,12.37,3.3,2.59,7.66,3.77,12.85,3.77,4.01,0,7.54-.71,10.84-2,3.3-1.3,6.25-2.95,8.6-4.95.35.35,6.13,10.49,6.13,10.49-3.65,2.71-7.78,4.83-12.26,6.48-4.12,1.53-8.96,2.24-14.26,2.24-6.36,0-12.02-1.3-16.62-4.01-4.48-2.59-8.13-6.36-11.08-11.31-2.59-4.95-3.89-10.49-3.89-16.5s1.18-11.43,3.77-16.38ZM392.69,87.83h31.46c-.47-4.71-2-8.01-4.6-10.13-2.83-2.47-6.13-3.77-10.13-3.77s-7.66,1.3-10.84,3.54c-2.83,2.24-4.71,5.66-5.89,10.37Z" fill="#20434f"></path><path d="M508.5,87.36v36.77h-14.49v-35.47c0-4.83-1.06-8.25-3.3-10.49-2.12-2.59-5.3-3.77-9.66-3.77-2.83,0-5.19.71-7.54,2.24-2.24,1.18-4.01,3.18-5.19,5.66-1.06,2.36-1.77,5.19-1.77,8.6v33.23h-14.61v-39.24l-8.84-15.56,12.49-7.07,7.31,12.49c7.42-11.08,15.44-12.49,20.86-12.49,6.13,0,9.9,1.06,12.37,2.24,2.47,1.18,4.71,2.71,6.36,4.6,4.01,4.36,6.01,10.49,6.01,18.27Z" fill="#20434f"></path><path d="M585.22,120.95c-2.59,1.3-6.01,2.59-10.25,3.77-3.89.83-8.01,1.3-12.37,1.3-8.49,0-16.03-1.88-22.51-5.42-6.36-3.54-11.31-8.6-14.97-15.32-3.54-6.48-5.3-14.02-5.3-22.63s1.77-15.91,5.19-22.63c3.42-6.6,8.72-11.78,14.97-15.2,6.48-3.77,14.26-5.54,23.45-5.54,4.6,0,8.6.35,12.02,1.3,4.01.94,7.31,2.12,9.66,3.53,2.48,1.18,5.42,2.83,8.84,5.07l-7.43,12.61c-3.65-2.47-7.19-4.36-10.61-5.77-4.01-1.53-8.25-2.36-12.85-2.36-6.13,0-11.2,1.18-15.2,3.65-4.36,2.71-7.54,6.13-9.66,10.37-2.12,4.6-3.3,9.66-3.3,15.2s1.18,10.49,3.3,14.85c2.12,4.24,5.3,7.66,9.66,10.14,4.12,2.36,9.19,3.53,15.08,3.53,3.42,0,6.48-.35,9.31-1.06,3.06-.83,5.66-1.77,7.78-2.95,2.95-1.53,5.19-2.95,6.84-4.24l7.31,12.73c-3.53,2.12-6.48,3.89-8.96,5.07Z" fill="#20434f"></path><path d="M603,124.13V38.69h14.38v85.44h-14.38Z" fill="#20434f"></path><path d="M628.11,94.2c0-18.62,13.2-31.94,32.17-31.94s31.94,13.2,31.94,31.82-13.08,31.94-32.06,31.94-32.05-12.37-32.05-31.82ZM660.17,113.64c10.14,0,17.09-7.19,17.09-19.56s-6.95-19.56-17.09-19.56-17.21,7.9-17.21,19.56,6.84,19.56,17.21,19.56Z" fill="#20434f"></path><path d="M725.55,126.02c-6.95,0-12.49-2.12-16.73-6.72-4.01-4.59-6.01-10.84-6.01-18.62v-36.53h14.38v35.47c0,4.6,1.06,8.13,3.3,10.61,2.12,2.36,5.42,3.42,9.78,3.42,2.83,0,5.3-.59,7.54-1.89,2.24-1.3,3.89-3.3,5.07-5.77,1.3-2.59,1.88-5.54,1.88-8.6v-33.23h14.5v39.6l8.72,15.2-12.37,7.07-6.95-11.9s-2.71,3.54-6.36,6.6c-4.48,3.77-9.19,5.3-16.73,5.3Z" fill="#20434f"></path><path d="M776.31,77.82c2.71-5.3,5.89-9.19,10.25-11.43,4.36-2.71,9.43-4.24,14.85-4.24,4.6,0,8.37.94,11.67,2.59,3.3,1.65,6.36,3.77,8.84,6.95v-33h14.38v64.93l8.6,15.2-12.37,7.07-7.54-13.08s-5.19,7.31-11.9,10.61c-2.83,1.41-7.31,2.48-11.55,2.48-5.54,0-10.61-1.3-14.97-4.13-4.24-2.24-7.54-6.13-10.25-11.08-2.48-4.95-3.53-10.25-3.53-16.5s1.06-11.78,3.53-16.38ZM787.5,94.2c0,4.01.71,7.19,2.12,9.9,1.65,3.3,3.77,5.3,6.01,6.72,2.59,1.53,5.42,2.36,8.96,2.36s6.6-.83,9.07-2.36c2.47-1.41,4.59-3.54,6.13-6.72,1.42-2.71,2.12-5.89,2.12-9.9,0-5.89-1.53-10.84-4.83-13.91-2.83-3.53-7.19-5.42-12.37-5.42s-9.43,1.89-12.37,5.42c-3.3,3.06-4.83,8.01-4.83,13.91Z" fill="#20434f"></path><polygon points="69.63 129.25 76.91 125.05 76.91 94.64 103.09 79.52 103.09 71.14 95.81 66.94 69.46 82.15 43.47 67.15 36.19 71.35 36.19 79.73 62.37 94.85 62.37 125.06 69.63 129.25" fill="#20434f"></polygon><polygon points="136.44 41.4 69.64 2.83 69.64 2.84 69.64 2.83 2.83 41.4 2.83 58.19 69.64 19.62 136.44 58.19 136.44 41.4" fill="#20434f"></polygon><polygon points="136.44 120.9 69.64 159.47 2.84 120.9 2.84 137.69 69.64 176.26 69.64 176.25 69.64 176.26 136.44 137.69 136.44 120.9" fill="#20434f"></polygon></svg>
  
      <svg class="logo__mobile" xmlns="http://www.w3.org/2000/svg" width="200" height="45" viewBox="0 0 847.73 179.09"><path d="M226.76,120.48c-12.96-7.31-20.51-20.74-20.51-37.59,0-8.48,1.77-16.03,5.42-22.63,7.07-13.2,20.51-20.98,37.36-20.98,8.37,0,15.67,1.89,22.16,5.54,12.85,7.42,20.27,21.09,20.27,38.06,0,8.37-1.77,15.91-5.3,22.39-7.07,13.08-20.51,20.74-37.12,20.74-8.37,0-15.79-1.77-22.27-5.54ZM248.92,112.46c16.5,0,27.34-11.55,27.34-29.58s-11.43-30.17-27.34-30.17-27.46,11.67-27.46,30.17,10.96,29.58,27.46,29.58Z" fill="#20434f"></path><path d="M310.48,62.26l7.78,13.67c7.07-11.2,16.38-13.67,23.57-13.67,5.77,0,10.72,1.3,15.08,4.12,4.48,2.95,7.9,6.72,10.14,11.43,2.47,4.95,3.65,10.37,3.65,16.38s-1.18,11.55-3.65,16.5c-2.24,4.71-5.78,8.49-10.25,11.2-4.24,2.83-9.19,4.12-14.97,4.12-3.89,0-7.78-.82-11.55-2.47-3.42-1.65-6.48-4.01-8.96-6.95v29.93h-14.38v-61.63l-8.84-15.44,12.37-7.19ZM321.33,94.2c0,3.65.71,7.07,2.12,10.02,1.77,3.18,3.77,5.42,6.13,6.84,2.71,1.53,5.66,2.24,9.07,2.24s6.48-.71,9.07-2.24c2.59-1.53,4.71-3.77,6.01-6.84,1.53-2.95,2.12-6.36,2.12-10.02,0-5.89-1.53-10.6-4.59-13.91-3.18-3.53-7.31-5.3-12.73-5.3-5.07,0-9.31,1.77-12.49,5.3-3.06,3.3-4.71,8.01-4.71,13.91Z" fill="#20434f"></path><path d="M382.08,77.82c2.36-4.71,5.89-8.6,10.72-11.67,4.95-2.71,10.37-4.01,16.62-4.01s11.43,1.3,15.56,3.77c4.48,2.83,7.78,6.6,10.14,11.31,2.12,4.83,3.3,10.61,3.3,16.97l-.23,3.42h-45.84c.47,5.3,2.36,9.31,5.66,12.37,3.3,2.59,7.66,3.77,12.85,3.77,4.01,0,7.54-.71,10.84-2,3.3-1.3,6.25-2.95,8.6-4.95.35.35,6.13,10.49,6.13,10.49-3.65,2.71-7.78,4.83-12.26,6.48-4.12,1.53-8.96,2.24-14.26,2.24-6.36,0-12.02-1.3-16.62-4.01-4.48-2.59-8.13-6.36-11.08-11.31-2.59-4.95-3.89-10.49-3.89-16.5s1.18-11.43,3.77-16.38ZM392.69,87.83h31.46c-.47-4.71-2-8.01-4.6-10.13-2.83-2.47-6.13-3.77-10.13-3.77s-7.66,1.3-10.84,3.54c-2.83,2.24-4.71,5.66-5.89,10.37Z" fill="#20434f"></path><path d="M508.5,87.36v36.77h-14.49v-35.47c0-4.83-1.06-8.25-3.3-10.49-2.12-2.59-5.3-3.77-9.66-3.77-2.83,0-5.19.71-7.54,2.24-2.24,1.18-4.01,3.18-5.19,5.66-1.06,2.36-1.77,5.19-1.77,8.6v33.23h-14.61v-39.24l-8.84-15.56,12.49-7.07,7.31,12.49c7.42-11.08,15.44-12.49,20.86-12.49,6.13,0,9.9,1.06,12.37,2.24,2.47,1.18,4.71,2.71,6.36,4.6,4.01,4.36,6.01,10.49,6.01,18.27Z" fill="#20434f"></path><path d="M585.22,120.95c-2.59,1.3-6.01,2.59-10.25,3.77-3.89.83-8.01,1.3-12.37,1.3-8.49,0-16.03-1.88-22.51-5.42-6.36-3.54-11.31-8.6-14.97-15.32-3.54-6.48-5.3-14.02-5.3-22.63s1.77-15.91,5.19-22.63c3.42-6.6,8.72-11.78,14.97-15.2,6.48-3.77,14.26-5.54,23.45-5.54,4.6,0,8.6.35,12.02,1.3,4.01.94,7.31,2.12,9.66,3.53,2.48,1.18,5.42,2.83,8.84,5.07l-7.43,12.61c-3.65-2.47-7.19-4.36-10.61-5.77-4.01-1.53-8.25-2.36-12.85-2.36-6.13,0-11.2,1.18-15.2,3.65-4.36,2.71-7.54,6.13-9.66,10.37-2.12,4.6-3.3,9.66-3.3,15.2s1.18,10.49,3.3,14.85c2.12,4.24,5.3,7.66,9.66,10.14,4.12,2.36,9.19,3.53,15.08,3.53,3.42,0,6.48-.35,9.31-1.06,3.06-.83,5.66-1.77,7.78-2.95,2.95-1.53,5.19-2.95,6.84-4.24l7.31,12.73c-3.53,2.12-6.48,3.89-8.96,5.07Z" fill="#20434f"></path><path d="M603,124.13V38.69h14.38v85.44h-14.38Z" fill="#20434f"></path><path d="M628.11,94.2c0-18.62,13.2-31.94,32.17-31.94s31.94,13.2,31.94,31.82-13.08,31.94-32.06,31.94-32.05-12.37-32.05-31.82ZM660.17,113.64c10.14,0,17.09-7.19,17.09-19.56s-6.95-19.56-17.09-19.56-17.21,7.9-17.21,19.56,6.84,19.56,17.21,19.56Z" fill="#20434f"></path><path d="M725.55,126.02c-6.95,0-12.49-2.12-16.73-6.72-4.01-4.59-6.01-10.84-6.01-18.62v-36.53h14.38v35.47c0,4.6,1.06,8.13,3.3,10.61,2.12,2.36,5.42,3.42,9.78,3.42,2.83,0,5.3-.59,7.54-1.89,2.24-1.3,3.89-3.3,5.07-5.77,1.3-2.59,1.88-5.54,1.88-8.6v-33.23h14.5v39.6l8.72,15.2-12.37,7.07-6.95-11.9s-2.71,3.54-6.36,6.6c-4.48,3.77-9.19,5.3-16.73,5.3Z" fill="#20434f"></path><path d="M776.31,77.82c2.71-5.3,5.89-9.19,10.25-11.43,4.36-2.71,9.43-4.24,14.85-4.24,4.6,0,8.37.94,11.67,2.59,3.3,1.65,6.36,3.77,8.84,6.95v-33h14.38v64.93l8.6,15.2-12.37,7.07-7.54-13.08s-5.19,7.31-11.9,10.61c-2.83,1.41-7.31,2.48-11.55,2.48-5.54,0-10.61-1.3-14.97-4.13-4.24-2.24-7.54-6.13-10.25-11.08-2.48-4.95-3.53-10.25-3.53-16.5s1.06-11.78,3.53-16.38ZM787.5,94.2c0,4.01.71,7.19,2.12,9.9,1.65,3.3,3.77,5.3,6.01,6.72,2.59,1.53,5.42,2.36,8.96,2.36s6.6-.83,9.07-2.36c2.47-1.41,4.59-3.54,6.13-6.72,1.42-2.71,2.12-5.89,2.12-9.9,0-5.89-1.53-10.84-4.83-13.91-2.83-3.53-7.19-5.42-12.37-5.42s-9.43,1.89-12.37,5.42c-3.3,3.06-4.83,8.01-4.83,13.91Z" fill="#20434f"></path><polygon points="69.63 129.25 76.91 125.05 76.91 94.64 103.09 79.52 103.09 71.14 95.81 66.94 69.46 82.15 43.47 67.15 36.19 71.35 36.19 79.73 62.37 94.85 62.37 125.06 69.63 129.25" fill="#20434f"></polygon><polygon points="136.44 41.4 69.64 2.83 69.64 2.84 69.64 2.83 2.83 41.4 2.83 58.19 69.64 19.62 136.44 58.19 136.44 41.4" fill="#20434f"></polygon><polygon points="136.44 120.9 69.64 159.47 2.84 120.9 2.84 137.69 69.64 176.26 69.64 176.25 69.64 176.26 136.44 137.69 136.44 120.9" fill="#20434f"></polygon></svg>
  </a>
        </div>
      </div>
      <div class="headarea__col">
        <div class="headarea__menu">
          



    <div class="mega-menu mega-menu--init mega-menu--inited">
          <ul class="mega-menu__links">
                        <li class="mega-menu__main-item">
                        <span href="" class="mega-menu__main-link">Lösungen</span>
            <div class="mega-menu__overlay">              <div class="mega-menu__overlay-content">
                <div class="mega-menu__overlay-left">
                  <h3 class="mega-menu__headline">Lösungen</h3>
                  <div class="mega-menu__subline">  OpenCloud unterstützt Organisationen dabei, ihr Wissen besser nutzbar zu machen.
</div>
                </div>
                <div class="mega-menu__overlay-right">
                                      <ul class="mega-menu__level-1">
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/loesungen/oeffentlicher-sektor">Öffentlicher Sektor</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/loesungen/forschung-wissenschaft">Forschung &amp; Wissenschaft</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/loesungen/bildung">Bildung</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/loesungen/unternehmen">Unternehmen</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/loesungen/sicherheit">Sicherheit</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/loesungen/provider">Provider</a>
                                                                            </li>
                                          </ul>
                                  </div>
              </div>
            </div></li>
                                    <li class="mega-menu__main-item">
                        <span href="" class="mega-menu__main-link">Produkt</span>
            <div class="mega-menu__overlay">              <div class="mega-menu__overlay-content">
                <div class="mega-menu__overlay-left">
                  <h3 class="mega-menu__headline">Produkt</h3>
                  <div class="mega-menu__subline">  OpenCloud ist exzellentes Filemanagement &amp; Sharing mit nahtloser Kollaboration.
</div>
                </div>
                <div class="mega-menu__overlay-right">
                                      <ul class="mega-menu__level-1">
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/funktionen">Funktionen</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/produkt/download-apps">Download Apps</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/produkt/migration">Migration</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/Subskription-support">Preise</a>
                                                                            </li>
                                          </ul>
                                  </div>
              </div>
            </div></li>
                                    <li class="mega-menu__main-item">
                        <span href="" class="mega-menu__main-link">Ressourcen</span>
            <div class="mega-menu__overlay">              <div class="mega-menu__overlay-content">
                <div class="mega-menu__overlay-left">
                  <h3 class="mega-menu__headline">Ressourcen</h3>
                  <div class="mega-menu__subline">  Als neues Teammitglied macht OpenCloud die Zusammenarbeit flexibel, einfach und zukunftssicher.
</div>
                </div>
                <div class="mega-menu__overlay-right">
                                      <ul class="mega-menu__level-1">
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/aktuelles">Blog &amp; News</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://docs.opencloud.eu/">Dokumentation</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://github.com/opencloud-eu">GitHub</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/wissenswertes">Wissenswertes</a>
                                                                            </li>
                                          </ul>
                                  </div>
              </div>
            </div></li>
                                    <li class="mega-menu__main-item">
                        <span href="" class="mega-menu__main-link">Community</span>
            <div class="mega-menu__overlay">              <div class="mega-menu__overlay-content">
                <div class="mega-menu__overlay-left">
                  <h3 class="mega-menu__headline">Community</h3>
                  <div class="mega-menu__subline">  Lasst uns zusammen eine große, vitale Community für digitale Souveränität bauen.
</div>
                </div>
                <div class="mega-menu__overlay-right">
                                      <ul class="mega-menu__level-1">
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/opencloud-community">OpenCloud Community</a>
                                                                            </li>
                                          </ul>
                                  </div>
              </div>
            </div></li>
                                    <li class="mega-menu__main-item ">
                        <span href="" class="mega-menu__main-link">Über uns</span>
            <div class="mega-menu__overlay">              <div class="mega-menu__overlay-content">
                <div class="mega-menu__overlay-left">
                  <h3 class="mega-menu__headline">Über uns</h3>
                  <div class="mega-menu__subline">  OpenSource ist unsere DNA. Mit Rückenwind aus 30 Jahren IT-Erfahrung setzen wir uns für freie Kommunikation ein.
</div>
                </div>
                <div class="mega-menu__overlay-right">
                                      <ul class="mega-menu__level-1">
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/ueber-uns/unternehmen">Unternehmen</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/ueber-uns/karriere-jobs">Karriere / Jobs</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/ueber-uns/partner">Partner</a>
                                                                            </li>
                                              <li class="mega-menu__item ">
                                                      <a class="mega-menu__link" href="https://opencloud.eu/de/ueber-uns/presse">Presse</a>
                                                                            </li>
                                          </ul>
                                  </div>
              </div>
            </div></li>
                        </ul>
      </div>




        </div>
      </div>
            <div class="headarea__col">
        <label class="headarea__drawer-label" for="drawer-open">
                      <svg class="headarea__drawer-icon" viewBox="0 0 21 18" width="21" height="18">
              <rect class="headarea__firstline" width="21" height="2" fill="var(--petrol)"></rect>
              <rect class="headarea__secondline" y="8" width="21" height="2" fill="var(--petrol)"></rect>
              <rect class="headarea__thirdline" y="16" width="21" height="2" fill="var(--petrol)"></rect>
            </svg>
                  </label>
      </div>
      <div class="headarea__col headarea__col--buttons">
        <div class="headarea__support">
          


    <a href="https://opencloud.eu/de/demo" class="button button--hollow button--link button--init button--inited">
    Demo
  </a>

          


    <a href="https://opencloud.eu/de/kontakt" class="button button--link button--init button--inited">
    Kontakt
  </a>
        </div>
      </div>
    </div>
    <input class="headarea__toggler" type="checkbox" hidden="" id="drawer-open">

        <div class="headarea__drawer">
      <div class="headarea__row">
        <div class="headarea__col">
          <div class="headarea__logo">
            


<a href="https://opencloud.eu/de" class="logo ">
      <svg class="logo__svg" xmlns="http://www.w3.org/2000/svg" width="195" height="43" viewBox="0 0 847.73 179.09"><path d="M226.76,120.48c-12.96-7.31-20.51-20.74-20.51-37.59,0-8.48,1.77-16.03,5.42-22.63,7.07-13.2,20.51-20.98,37.36-20.98,8.37,0,15.67,1.89,22.16,5.54,12.85,7.42,20.27,21.09,20.27,38.06,0,8.37-1.77,15.91-5.3,22.39-7.07,13.08-20.51,20.74-37.12,20.74-8.37,0-15.79-1.77-22.27-5.54ZM248.92,112.46c16.5,0,27.34-11.55,27.34-29.58s-11.43-30.17-27.34-30.17-27.46,11.67-27.46,30.17,10.96,29.58,27.46,29.58Z" fill="#20434f"></path><path d="M310.48,62.26l7.78,13.67c7.07-11.2,16.38-13.67,23.57-13.67,5.77,0,10.72,1.3,15.08,4.12,4.48,2.95,7.9,6.72,10.14,11.43,2.47,4.95,3.65,10.37,3.65,16.38s-1.18,11.55-3.65,16.5c-2.24,4.71-5.78,8.49-10.25,11.2-4.24,2.83-9.19,4.12-14.97,4.12-3.89,0-7.78-.82-11.55-2.47-3.42-1.65-6.48-4.01-8.96-6.95v29.93h-14.38v-61.63l-8.84-15.44,12.37-7.19ZM321.33,94.2c0,3.65.71,7.07,2.12,10.02,1.77,3.18,3.77,5.42,6.13,6.84,2.71,1.53,5.66,2.24,9.07,2.24s6.48-.71,9.07-2.24c2.59-1.53,4.71-3.77,6.01-6.84,1.53-2.95,2.12-6.36,2.12-10.02,0-5.89-1.53-10.6-4.59-13.91-3.18-3.53-7.31-5.3-12.73-5.3-5.07,0-9.31,1.77-12.49,5.3-3.06,3.3-4.71,8.01-4.71,13.91Z" fill="#20434f"></path><path d="M382.08,77.82c2.36-4.71,5.89-8.6,10.72-11.67,4.95-2.71,10.37-4.01,16.62-4.01s11.43,1.3,15.56,3.77c4.48,2.83,7.78,6.6,10.14,11.31,2.12,4.83,3.3,10.61,3.3,16.97l-.23,3.42h-45.84c.47,5.3,2.36,9.31,5.66,12.37,3.3,2.59,7.66,3.77,12.85,3.77,4.01,0,7.54-.71,10.84-2,3.3-1.3,6.25-2.95,8.6-4.95.35.35,6.13,10.49,6.13,10.49-3.65,2.71-7.78,4.83-12.26,6.48-4.12,1.53-8.96,2.24-14.26,2.24-6.36,0-12.02-1.3-16.62-4.01-4.48-2.59-8.13-6.36-11.08-11.31-2.59-4.95-3.89-10.49-3.89-16.5s1.18-11.43,3.77-16.38ZM392.69,87.83h31.46c-.47-4.71-2-8.01-4.6-10.13-2.83-2.47-6.13-3.77-10.13-3.77s-7.66,1.3-10.84,3.54c-2.83,2.24-4.71,5.66-5.89,10.37Z" fill="#20434f"></path><path d="M508.5,87.36v36.77h-14.49v-35.47c0-4.83-1.06-8.25-3.3-10.49-2.12-2.59-5.3-3.77-9.66-3.77-2.83,0-5.19.71-7.54,2.24-2.24,1.18-4.01,3.18-5.19,5.66-1.06,2.36-1.77,5.19-1.77,8.6v33.23h-14.61v-39.24l-8.84-15.56,12.49-7.07,7.31,12.49c7.42-11.08,15.44-12.49,20.86-12.49,6.13,0,9.9,1.06,12.37,2.24,2.47,1.18,4.71,2.71,6.36,4.6,4.01,4.36,6.01,10.49,6.01,18.27Z" fill="#20434f"></path><path d="M585.22,120.95c-2.59,1.3-6.01,2.59-10.25,3.77-3.89.83-8.01,1.3-12.37,1.3-8.49,0-16.03-1.88-22.51-5.42-6.36-3.54-11.31-8.6-14.97-15.32-3.54-6.48-5.3-14.02-5.3-22.63s1.77-15.91,5.19-22.63c3.42-6.6,8.72-11.78,14.97-15.2,6.48-3.77,14.26-5.54,23.45-5.54,4.6,0,8.6.35,12.02,1.3,4.01.94,7.31,2.12,9.66,3.53,2.48,1.18,5.42,2.83,8.84,5.07l-7.43,12.61c-3.65-2.47-7.19-4.36-10.61-5.77-4.01-1.53-8.25-2.36-12.85-2.36-6.13,0-11.2,1.18-15.2,3.65-4.36,2.71-7.54,6.13-9.66,10.37-2.12,4.6-3.3,9.66-3.3,15.2s1.18,10.49,3.3,14.85c2.12,4.24,5.3,7.66,9.66,10.14,4.12,2.36,9.19,3.53,15.08,3.53,3.42,0,6.48-.35,9.31-1.06,3.06-.83,5.66-1.77,7.78-2.95,2.95-1.53,5.19-2.95,6.84-4.24l7.31,12.73c-3.53,2.12-6.48,3.89-8.96,5.07Z" fill="#20434f"></path><path d="M603,124.13V38.69h14.38v85.44h-14.38Z" fill="#20434f"></path><path d="M628.11,94.2c0-18.62,13.2-31.94,32.17-31.94s31.94,13.2,31.94,31.82-13.08,31.94-32.06,31.94-32.05-12.37-32.05-31.82ZM660.17,113.64c10.14,0,17.09-7.19,17.09-19.56s-6.95-19.56-17.09-19.56-17.21,7.9-17.21,19.56,6.84,19.56,17.21,19.56Z" fill="#20434f"></path><path d="M725.55,126.02c-6.95,0-12.49-2.12-16.73-6.72-4.01-4.59-6.01-10.84-6.01-18.62v-36.53h14.38v35.47c0,4.6,1.06,8.13,3.3,10.61,2.12,2.36,5.42,3.42,9.78,3.42,2.83,0,5.3-.59,7.54-1.89,2.24-1.3,3.89-3.3,5.07-5.77,1.3-2.59,1.88-5.54,1.88-8.6v-33.23h14.5v39.6l8.72,15.2-12.37,7.07-6.95-11.9s-2.71,3.54-6.36,6.6c-4.48,3.77-9.19,5.3-16.73,5.3Z" fill="#20434f"></path><path d="M776.31,77.82c2.71-5.3,5.89-9.19,10.25-11.43,4.36-2.71,9.43-4.24,14.85-4.24,4.6,0,8.37.94,11.67,2.59,3.3,1.65,6.36,3.77,8.84,6.95v-33h14.38v64.93l8.6,15.2-12.37,7.07-7.54-13.08s-5.19,7.31-11.9,10.61c-2.83,1.41-7.31,2.48-11.55,2.48-5.54,0-10.61-1.3-14.97-4.13-4.24-2.24-7.54-6.13-10.25-11.08-2.48-4.95-3.53-10.25-3.53-16.5s1.06-11.78,3.53-16.38ZM787.5,94.2c0,4.01.71,7.19,2.12,9.9,1.65,3.3,3.77,5.3,6.01,6.72,2.59,1.53,5.42,2.36,8.96,2.36s6.6-.83,9.07-2.36c2.47-1.41,4.59-3.54,6.13-6.72,1.42-2.71,2.12-5.89,2.12-9.9,0-5.89-1.53-10.84-4.83-13.91-2.83-3.53-7.19-5.42-12.37-5.42s-9.43,1.89-12.37,5.42c-3.3,3.06-4.83,8.01-4.83,13.91Z" fill="#20434f"></path><polygon points="69.63 129.25 76.91 125.05 76.91 94.64 103.09 79.52 103.09 71.14 95.81 66.94 69.46 82.15 43.47 67.15 36.19 71.35 36.19 79.73 62.37 94.85 62.37 125.06 69.63 129.25" fill="#20434f"></polygon><polygon points="136.44 41.4 69.64 2.83 69.64 2.84 69.64 2.83 2.83 41.4 2.83 58.19 69.64 19.62 136.44 58.19 136.44 41.4" fill="#20434f"></polygon><polygon points="136.44 120.9 69.64 159.47 2.84 120.9 2.84 137.69 69.64 176.26 69.64 176.25 69.64 176.26 136.44 137.69 136.44 120.9" fill="#20434f"></polygon></svg>
  
      <svg class="logo__mobile" xmlns="http://www.w3.org/2000/svg" width="200" height="45" viewBox="0 0 847.73 179.09"><path d="M226.76,120.48c-12.96-7.31-20.51-20.74-20.51-37.59,0-8.48,1.77-16.03,5.42-22.63,7.07-13.2,20.51-20.98,37.36-20.98,8.37,0,15.67,1.89,22.16,5.54,12.85,7.42,20.27,21.09,20.27,38.06,0,8.37-1.77,15.91-5.3,22.39-7.07,13.08-20.51,20.74-37.12,20.74-8.37,0-15.79-1.77-22.27-5.54ZM248.92,112.46c16.5,0,27.34-11.55,27.34-29.58s-11.43-30.17-27.34-30.17-27.46,11.67-27.46,30.17,10.96,29.58,27.46,29.58Z" fill="#20434f"></path><path d="M310.48,62.26l7.78,13.67c7.07-11.2,16.38-13.67,23.57-13.67,5.77,0,10.72,1.3,15.08,4.12,4.48,2.95,7.9,6.72,10.14,11.43,2.47,4.95,3.65,10.37,3.65,16.38s-1.18,11.55-3.65,16.5c-2.24,4.71-5.78,8.49-10.25,11.2-4.24,2.83-9.19,4.12-14.97,4.12-3.89,0-7.78-.82-11.55-2.47-3.42-1.65-6.48-4.01-8.96-6.95v29.93h-14.38v-61.63l-8.84-15.44,12.37-7.19ZM321.33,94.2c0,3.65.71,7.07,2.12,10.02,1.77,3.18,3.77,5.42,6.13,6.84,2.71,1.53,5.66,2.24,9.07,2.24s6.48-.71,9.07-2.24c2.59-1.53,4.71-3.77,6.01-6.84,1.53-2.95,2.12-6.36,2.12-10.02,0-5.89-1.53-10.6-4.59-13.91-3.18-3.53-7.31-5.3-12.73-5.3-5.07,0-9.31,1.77-12.49,5.3-3.06,3.3-4.71,8.01-4.71,13.91Z" fill="#20434f"></path><path d="M382.08,77.82c2.36-4.71,5.89-8.6,10.72-11.67,4.95-2.71,10.37-4.01,16.62-4.01s11.43,1.3,15.56,3.77c4.48,2.83,7.78,6.6,10.14,11.31,2.12,4.83,3.3,10.61,3.3,16.97l-.23,3.42h-45.84c.47,5.3,2.36,9.31,5.66,12.37,3.3,2.59,7.66,3.77,12.85,3.77,4.01,0,7.54-.71,10.84-2,3.3-1.3,6.25-2.95,8.6-4.95.35.35,6.13,10.49,6.13,10.49-3.65,2.71-7.78,4.83-12.26,6.48-4.12,1.53-8.96,2.24-14.26,2.24-6.36,0-12.02-1.3-16.62-4.01-4.48-2.59-8.13-6.36-11.08-11.31-2.59-4.95-3.89-10.49-3.89-16.5s1.18-11.43,3.77-16.38ZM392.69,87.83h31.46c-.47-4.71-2-8.01-4.6-10.13-2.83-2.47-6.13-3.77-10.13-3.77s-7.66,1.3-10.84,3.54c-2.83,2.24-4.71,5.66-5.89,10.37Z" fill="#20434f"></path><path d="M508.5,87.36v36.77h-14.49v-35.47c0-4.83-1.06-8.25-3.3-10.49-2.12-2.59-5.3-3.77-9.66-3.77-2.83,0-5.19.71-7.54,2.24-2.24,1.18-4.01,3.18-5.19,5.66-1.06,2.36-1.77,5.19-1.77,8.6v33.23h-14.61v-39.24l-8.84-15.56,12.49-7.07,7.31,12.49c7.42-11.08,15.44-12.49,20.86-12.49,6.13,0,9.9,1.06,12.37,2.24,2.47,1.18,4.71,2.71,6.36,4.6,4.01,4.36,6.01,10.49,6.01,18.27Z" fill="#20434f"></path><path d="M585.22,120.95c-2.59,1.3-6.01,2.59-10.25,3.77-3.89.83-8.01,1.3-12.37,1.3-8.49,0-16.03-1.88-22.51-5.42-6.36-3.54-11.31-8.6-14.97-15.32-3.54-6.48-5.3-14.02-5.3-22.63s1.77-15.91,5.19-22.63c3.42-6.6,8.72-11.78,14.97-15.2,6.48-3.77,14.26-5.54,23.45-5.54,4.6,0,8.6.35,12.02,1.3,4.01.94,7.31,2.12,9.66,3.53,2.48,1.18,5.42,2.83,8.84,5.07l-7.43,12.61c-3.65-2.47-7.19-4.36-10.61-5.77-4.01-1.53-8.25-2.36-12.85-2.36-6.13,0-11.2,1.18-15.2,3.65-4.36,2.71-7.54,6.13-9.66,10.37-2.12,4.6-3.3,9.66-3.3,15.2s1.18,10.49,3.3,14.85c2.12,4.24,5.3,7.66,9.66,10.14,4.12,2.36,9.19,3.53,15.08,3.53,3.42,0,6.48-.35,9.31-1.06,3.06-.83,5.66-1.77,7.78-2.95,2.95-1.53,5.19-2.95,6.84-4.24l7.31,12.73c-3.53,2.12-6.48,3.89-8.96,5.07Z" fill="#20434f"></path><path d="M603,124.13V38.69h14.38v85.44h-14.38Z" fill="#20434f"></path><path d="M628.11,94.2c0-18.62,13.2-31.94,32.17-31.94s31.94,13.2,31.94,31.82-13.08,31.94-32.06,31.94-32.05-12.37-32.05-31.82ZM660.17,113.64c10.14,0,17.09-7.19,17.09-19.56s-6.95-19.56-17.09-19.56-17.21,7.9-17.21,19.56,6.84,19.56,17.21,19.56Z" fill="#20434f"></path><path d="M725.55,126.02c-6.95,0-12.49-2.12-16.73-6.72-4.01-4.59-6.01-10.84-6.01-18.62v-36.53h14.38v35.47c0,4.6,1.06,8.13,3.3,10.61,2.12,2.36,5.42,3.42,9.78,3.42,2.83,0,5.3-.59,7.54-1.89,2.24-1.3,3.89-3.3,5.07-5.77,1.3-2.59,1.88-5.54,1.88-8.6v-33.23h14.5v39.6l8.72,15.2-12.37,7.07-6.95-11.9s-2.71,3.54-6.36,6.6c-4.48,3.77-9.19,5.3-16.73,5.3Z" fill="#20434f"></path><path d="M776.31,77.82c2.71-5.3,5.89-9.19,10.25-11.43,4.36-2.71,9.43-4.24,14.85-4.24,4.6,0,8.37.94,11.67,2.59,3.3,1.65,6.36,3.77,8.84,6.95v-33h14.38v64.93l8.6,15.2-12.37,7.07-7.54-13.08s-5.19,7.31-11.9,10.61c-2.83,1.41-7.31,2.48-11.55,2.48-5.54,0-10.61-1.3-14.97-4.13-4.24-2.24-7.54-6.13-10.25-11.08-2.48-4.95-3.53-10.25-3.53-16.5s1.06-11.78,3.53-16.38ZM787.5,94.2c0,4.01.71,7.19,2.12,9.9,1.65,3.3,3.77,5.3,6.01,6.72,2.59,1.53,5.42,2.36,8.96,2.36s6.6-.83,9.07-2.36c2.47-1.41,4.59-3.54,6.13-6.72,1.42-2.71,2.12-5.89,2.12-9.9,0-5.89-1.53-10.84-4.83-13.91-2.83-3.53-7.19-5.42-12.37-5.42s-9.43,1.89-12.37,5.42c-3.3,3.06-4.83,8.01-4.83,13.91Z" fill="#20434f"></path><polygon points="69.63 129.25 76.91 125.05 76.91 94.64 103.09 79.52 103.09 71.14 95.81 66.94 69.46 82.15 43.47 67.15 36.19 71.35 36.19 79.73 62.37 94.85 62.37 125.06 69.63 129.25" fill="#20434f"></polygon><polygon points="136.44 41.4 69.64 2.83 69.64 2.84 69.64 2.83 2.83 41.4 2.83 58.19 69.64 19.62 136.44 58.19 136.44 41.4" fill="#20434f"></polygon><polygon points="136.44 120.9 69.64 159.47 2.84 120.9 2.84 137.69 69.64 176.26 69.64 176.25 69.64 176.26 136.44 137.69 136.44 120.9" fill="#20434f"></polygon></svg>
  </a>
          </div>
        </div>
        <div class="headarea__col">
          <label class="headarea__drawer-label headarea__drawer-label--open" for="drawer-open">
            <svg class="headarea__drawer-icon" viewBox="0 0 21 18" width="21" height="18">
              <rect class="headarea__firstline" x="2" y="-2" width="21" height="2"></rect>
              <rect class="headarea__secondline" x="-9.5" y="11.5" width="21" height="2"></rect>
            </svg>
          </label>
        </div>
        <div class="headarea__col">
          <div class="headarea__support">
            


<a class="icon-button " name="Soforthilfe Button" href="https://opencloud.eu/de/kontakt">
  <span class="icon-button__text">
    Jetzt kontaktieren
  </span>
  <span class="icon-button__icon">📧︎</span>
</a>
          </div>
        </div>
      </div>
      <div>
  




  
  <div class="listview">
              <nav class="listview__view listview__view--root" id="listview-root">
                                                    <div class="listview__item">
                                                      <a class="listview__link listview__link--forward" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server#listview-menu_link_contentae03830a2-674e-490c-af49-ad6a8eb1afff">
                      Lösungen
                    </a>
                                                </div>
                                        <div class="listview__item">
                                                      <a class="listview__link listview__link--forward" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server#listview-menu_link_contenta1aa5cb6d-bfab-411b-b43b-6dc9761141fe">
                      Produkt
                    </a>
                                                </div>
                                        <div class="listview__item">
                                                      <a class="listview__link listview__link--forward" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server#listview-menu_link_contenta49017b32-9bd2-440b-874c-d1aa28200d64">
                      Ressourcen
                    </a>
                                                </div>
                                        <div class="listview__item">
                                                      <a class="listview__link listview__link--forward" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server#listview-menu_link_contenta87ba6abe-4b2a-4f52-9264-fa84d64c9345">
                      Community
                    </a>
                                                </div>
                                        <div class="listview__item">
                                                      <a class="listview__link listview__link--forward" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server#listview-menu_link_contenta51064039-5ad2-4e6b-b8d2-1acb088b5982">
                      Über uns
                    </a>
                                                </div>
                                                  </nav>          <nav class="listview__view listview__view--child" id="listview-menu_link_contentae03830a2-674e-490c-af49-ad6a8eb1afff" hidden="hidden">
                  <header class="listview__header">
            <a class="listview__link listview__link--back" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server#listview-root">
              <svg class="listview__arrow" xmlns="http://www.w3.org/2000/svg" width="30" height="18.54" viewBox="0 0 30 18.54"><polygon points="20.38 0 18.98 1.4 26.21 8.63 0 8.63 0 10.61 26.21 10.61 18.98 17.83 20.38 19.23 30 9.62 20.38 0"></polygon></svg>
              <span>
                                Lösungen
              </span>
            </a>
                          <div class="listview__description">  OpenCloud unterstützt Organisationen dabei, ihr Wissen besser nutzbar zu machen.
</div>
                      </header>
                                                    <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/loesungen/oeffentlicher-sektor">Öffentlicher Sektor</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/loesungen/forschung-wissenschaft">Forschung &amp; Wissenschaft</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/loesungen/bildung">Bildung</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/loesungen/unternehmen">Unternehmen</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/loesungen/sicherheit">Sicherheit</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/loesungen/provider">Provider</a>
                              </div>
                                                  </nav>          <nav class="listview__view listview__view--child" id="listview-menu_link_contenta1aa5cb6d-bfab-411b-b43b-6dc9761141fe" hidden="hidden">
                  <header class="listview__header">
            <a class="listview__link listview__link--back" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server#listview-root">
              <svg class="listview__arrow" xmlns="http://www.w3.org/2000/svg" width="30" height="18.54" viewBox="0 0 30 18.54"><polygon points="20.38 0 18.98 1.4 26.21 8.63 0 8.63 0 10.61 26.21 10.61 18.98 17.83 20.38 19.23 30 9.62 20.38 0"></polygon></svg>
              <span>
                                Produkt
              </span>
            </a>
                          <div class="listview__description">  OpenCloud ist exzellentes Filemanagement &amp; Sharing mit nahtloser Kollaboration.
</div>
                      </header>
                                                    <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/funktionen">Funktionen</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/produkt/download-apps">Download Apps</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/produkt/migration">Migration</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/Subskription-support">Preise</a>
                              </div>
                                                  </nav>          <nav class="listview__view listview__view--child" id="listview-menu_link_contenta49017b32-9bd2-440b-874c-d1aa28200d64" hidden="hidden">
                  <header class="listview__header">
            <a class="listview__link listview__link--back" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server#listview-root">
              <svg class="listview__arrow" xmlns="http://www.w3.org/2000/svg" width="30" height="18.54" viewBox="0 0 30 18.54"><polygon points="20.38 0 18.98 1.4 26.21 8.63 0 8.63 0 10.61 26.21 10.61 18.98 17.83 20.38 19.23 30 9.62 20.38 0"></polygon></svg>
              <span>
                                Ressourcen
              </span>
            </a>
                          <div class="listview__description">  Als neues Teammitglied macht OpenCloud die Zusammenarbeit flexibel, einfach und zukunftssicher.
</div>
                      </header>
                                                    <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/aktuelles">Blog &amp; News</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://docs.opencloud.eu/">Dokumentation</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://github.com/opencloud-eu">GitHub</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/wissenswertes">Wissenswertes</a>
                              </div>
                                                  </nav>          <nav class="listview__view listview__view--child" id="listview-menu_link_contenta87ba6abe-4b2a-4f52-9264-fa84d64c9345" hidden="hidden">
                  <header class="listview__header">
            <a class="listview__link listview__link--back" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server#listview-root">
              <svg class="listview__arrow" xmlns="http://www.w3.org/2000/svg" width="30" height="18.54" viewBox="0 0 30 18.54"><polygon points="20.38 0 18.98 1.4 26.21 8.63 0 8.63 0 10.61 26.21 10.61 18.98 17.83 20.38 19.23 30 9.62 20.38 0"></polygon></svg>
              <span>
                                Community
              </span>
            </a>
                          <div class="listview__description">  Lasst uns zusammen eine große, vitale Community für digitale Souveränität bauen.
</div>
                      </header>
                                                    <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/opencloud-community">OpenCloud Community</a>
                              </div>
                                                  </nav>          <nav class="listview__view listview__view--child" id="listview-menu_link_contenta51064039-5ad2-4e6b-b8d2-1acb088b5982" hidden="hidden">
                  <header class="listview__header">
            <a class="listview__link listview__link--back" href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server#listview-root">
              <svg class="listview__arrow" xmlns="http://www.w3.org/2000/svg" width="30" height="18.54" viewBox="0 0 30 18.54"><polygon points="20.38 0 18.98 1.4 26.21 8.63 0 8.63 0 10.61 26.21 10.61 18.98 17.83 20.38 19.23 30 9.62 20.38 0"></polygon></svg>
              <span>
                                Über uns
              </span>
            </a>
                          <div class="listview__description">  OpenSource ist unsere DNA. Mit Rückenwind aus 30 Jahren IT-Erfahrung setzen wir uns für freie Kommunikation ein.
</div>
                      </header>
                                                    <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/ueber-uns/unternehmen">Unternehmen</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/ueber-uns/karriere-jobs">Karriere / Jobs</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/ueber-uns/partner">Partner</a>
                              </div>
                                        <div class="listview__item">
                                  <a class="listview__link" href="https://opencloud.eu/de/ueber-uns/presse">Presse</a>
                              </div>
                                                  </nav>
  </div>
</div>




    </div>
  </div>
</div>
  </div>

      <div class="sheet__mood ">
      
    </div>
  
  <div class="sheet__admin">
    <div data-drupal-messages-fallback="" class="hidden"></div>


  </div>

  <div class="sheet__content">
        <div id="block-cloudy-hauptseiteninhalt">
  
    
        



<section data-history-node-id="2176" data-component-id="cloudy:oracle" class="oracle oracle--smaller">
  <div class="oracle__wrapper">
          <div class="oracle__top">
            


  <a class="back-button " href="https://opencloud.eu/de/wissenswertes">
    <svg class="back-button__svg" xmlns="http://www.w3.org/2000/svg" width="30" height="18.54" viewBox="0 0 30 18.54">
      <polygon points="20.38 0 18.98 1.4 26.21 8.63 0 8.63 0 10.61 26.21 10.61 18.98 17.83 20.38 19.23 30 9.62 20.38 0"></polygon>
    </svg>
    Wissenswertes zu IT-Sicherheit und mehr
  </a>
  
      </div>
        <div class="oracle__main">
          <time datetime="2025-08-14T12:00:00Z">14.08.2025</time>

 –   Blog


              <h2 class="oracle__title">  <span>OpenCloud installieren – ganz einfach auf dem eigenen Server</span>
</h2>
            
      <p>Sie möchten OpenCloud produktiv betreiben – mit eigener Domain, gültigen TLS-Zertifikaten und Weboffice? In diesem Artikel erfahren Sie Schritt für Schritt, wie Sie OpenCloud auf einem bestehenden Server einrichten und nahtlos in Ihre Infrastruktur integrieren.</p>
    </div>
        
      </div>
</section>




  


<div class="mantle mantle--limited            ">
  <div class="mantle__content">
                                <picture>
                  <source srcset="/sites/default/files/styles/858x543/public/2025-07/Blog_Install-OpenCloud_858x543.webp?itok=MN0YMfhd 1x" media="all and (min-width: 1025px)" type="image/webp" width="858" height="543">
              <source srcset="/sites/default/files/styles/858x543/public/2025-07/Blog_Install-OpenCloud_858x543.webp?itok=MN0YMfhd 1x" media="all and (min-width: 600px) and (max-width: 1024px)" type="image/webp" width="858" height="543">
              <source srcset="/sites/default/files/styles/550x407/public/2025-07/Blog_Install-OpenCloud_858x543.webp?itok=3vzFyRGW 1x" media="all and (max-width: 599px)" type="image/webp" width="550" height="407">
              <source srcset="/sites/default/files/styles/858x543/public/2025-07/Blog_Install-OpenCloud_858x543.jpg?itok=MN0YMfhd 1x" media="all and (min-width: 1025px)" type="image/jpeg" width="858" height="543">
              <source srcset="/sites/default/files/styles/858x543/public/2025-07/Blog_Install-OpenCloud_858x543.jpg?itok=MN0YMfhd 1x" media="all and (min-width: 600px) and (max-width: 1024px)" type="image/jpeg" width="858" height="543">
              <source srcset="/sites/default/files/styles/550x407/public/2025-07/Blog_Install-OpenCloud_858x543.jpg?itok=3vzFyRGW 1x" media="all and (max-width: 599px)" type="image/jpeg" width="550" height="407">
                  <img loading="lazy" width="1330" height="482" src="./opencloud_files/Blog_Install-OpenCloud_858x543.jpg" alt="OpenCloud installieren">

  </picture>


              
      
      </div>
  </div>

<div class="smaller-spaces">
        <div id="body-8613">
  
<section id="body-8613" data-component-id="cloudy:oracle" class="oracle">
  <div class="oracle__wrapper">
        <div class="oracle__main">
      
            
        <p>Wie <a href="https://docs.opencloud.eu/docs/admin/getting-started">unser Handbuch</a> beschreibt, lässt sich OpenCloud in ganz unterschiedlichen Szenarien einsetzen – vom lokalen Testsystem bis hin zum vollwertigen Cloud-Dienst mit Weboffice, Nutzerverwaltung und E-Mail-Anbindung. In diesem Artikel zeigen wir den Weg zur produktiven Bereitstellung: auf einem realen Server mit öffentlicher Domain, gültigen TLS-Zertifikaten und bestehenden Diensten wie etwa Apache.</p><p>Die Besonderheit: Wir installieren OpenCloud nicht auf der sprichwörtlichen „grünen Wiese“, sondern integrieren es in eine bereits laufende Umgebung mit Ubuntu 24.04 LTS – ohne andere Dienste zu stören. Unser Ziel: ein sicheres, containerbasiertes Setup mit Apache als Reverse Proxy, Docker Compose und allem, was für einen stabilen Produktivbetrieb dazugehört.</p><h4>Voraussetzungen für den eigenen OpenCloud-Server</h4><p>Damit Sie OpenCloud auf einem eigenen Server betreiben können, sind einige grundlegende Voraussetzungen nötig. Am besten eignet sich ein Root-Server oder vServer mit einer Linux-Distribution Ihrer Wahl. Wichtig ist dabei, dass Sie über vollständigen administrativen Zugriff verfügen, denn einige der Schritte erfordern root-Rechte.</p><p>Für den produktiven Betrieb sollten Sie außerdem folgende Punkte vorbereiten:</p><ul><li><strong>Eigene Domain</strong> mit passenden Subdomains wie cloud., collabora. und wopiserver., die auf die IP-Adresse Ihres Servers zeigen.</li><li><strong>TLS-Zertifikate</strong>, idealerweise von Let’s Encrypt, um die Dienste per HTTPS abzusichern.</li><li><strong>Docker und Docker Compose</strong>, da OpenCloud containerbasiert betrieben wird (mehr dazu im Abschnitt „Docker installieren: Die Grundlage für OpenCloud“).</li><li><strong>Apache oder ein anderer Webserver</strong>, der als Reverse Proxy zwischen Internet und Containern vermittelt.</li></ul><p>In unserem Beispiel haben wir OpenCloud auf einem Root-Server mit Ubuntu 24.04 LTS installiert. Ein Apache-Webserver war bereits eingerichtet und belegte die Ports 80 und 443 – daher haben wir auf Traefik verzichtet. Stattdessen nutzen wir Apache als Reverse Proxy für die OpenCloud-Dienste.</p><p>Folgende Subdomains wurden in der DNS-Zone konfiguriert und zeigen auf die Server-IP:</p><ul><li>blog.opencloud.rocks</li><li>cloud.blog.opencloud.rocks</li><li>collabora.blog.opencloud.rocks</li><li>wopiserver.blog.opencloud.rocks</li></ul><p>Ein gültiges Zertifikat für blog.opencloud.rocks war bereits vorhanden. Damit auch die Subdomains sicher erreichbar sind, haben wir vorab gültige TLS-Zertifikate für diese erstellt.</p><h4>TLS-Zertifikate für OpenCloud-Subdomains erstellen</h4><p>Damit Sie OpenCloud später über HTTPS nutzen können, brauchen alle benötigten Subdomains gültige TLS-Zertifikate. Da Apache als Reverse Proxy fungiert und die TLS-Terminierung übernimmt, kommt hier kein integrierter Proxy wie Traefik zum Einsatz.</p><p>Am einfachsten funktioniert die Zertifikatserstellung mit Let’s Encrypt. Für den Einsatz von certbot – dem offiziellen Client für Let’s Encrypt – muss Apache die Subdomains bereits bedienen können. Das eigentliche Ziel, etwa OpenCloud oder Collabora, spielt in diesem Moment noch keine Rolle. Entscheidend ist, dass Apache die Domain korrekt verarbeitet und auf HTTP-Anfragen antwortet. Dazu richten Sie Platzhalter-VirtualHosts ein, die einfache statische HTML-Seiten ausliefern.</p><p>Für jede Subdomain – in unserem Fall cloud.blog.opencloud.rocks, collabora.blog.opencloud.rocks und wopiserver.blog.opencloud.rocks – gibt es eine eigene Konfigurationsdatei in /etc/apache2/sites-available/. Ein VirtualHost für cloud.blog.opencloud.rocks könnte zum Beispiel so aussehen:</p><pre>&lt;VirtualHost *:80&gt;
    ServerName cloud.blog.opencloud.rocks
    DocumentRoot /var/www/placeholder-cloud

    &lt;Directory /var/www/placeholder-cloud&gt;
        Options -Indexes
        AllowOverride None
        Require all granted
    &lt;/Directory&gt;

    ErrorLog ${APACHE_LOG_DIR}/cloud_error.log
    CustomLog ${APACHE_LOG_DIR}/cloud_access.log combined
&lt;/VirtualHost&gt;
</pre><p>Damit Apache auf Anfragen reagiert, legen Sie das zugehörige Verzeichnis an und erstellen eine einfache Platzhalterseite:</p><pre>sudo mkdir -p /var/www/placeholder-cloud<br>
echo "OpenCloud-Vorbereitung" | sudo tee /var/www/placeholder-cloud/index.html
</pre><p>Im Anschluss aktivieren Sie die Site und laden die Konfiguration neu:</p><pre>sudo a2ensite cloud.blog.opencloud.rocks.conf
sudo systemctl reload apache2
</pre><p>Für collabora.blog.opencloud.rocks und wopiserver.blog.opencloud.rocks gehen Sie genauso vor – jeweils mit einem eigenen Verzeichnis (zum Beispiel /var/www/placeholder-collabora und /var/www/placeholder-wopiserver) und einer passenden VHost-Konfiguration.</p><p>Sind alle drei Subdomains erreichbar, fordern Sie mit certbot ein gemeinsames TLS-Zertifikat an:</p><pre>sudo certbot --apache \
  -d cloud.blog.opencloud.rocks \
  -d collabora.blog.opencloud.rocks \
  -d wopiserver.blog.opencloud.rocks
</pre><img src="./opencloud_files/certbot.png" alt="certbot" width="613" height="429"><p>certbot erkennt die bestehenden VHosts automatisch, führt die HTTP-01-Challenge durch und erweitert die Apache-Konfiguration um die nötigen TLS-Einstellungen. Für die Subdomains fordert certbot ein gemeinsames SAN-Zertifikat (Subject Alternative Names) an, das alle drei Subdomains abdeckt. Die erzeugten Zertifikate finden Sie anschließend im Verzeichnis /etc/letsencrypt/live/&lt;domain&gt;/; sie werden künftig automatisch verlängert.</p><h4>Apache als Reverse Proxy einrichten</h4><p>Sobald die TLS-Zertifikate eingerichtet sind, können Sie Apache so konfigurieren, dass HTTPS-Anfragen an die richtigen Dienste in Ihrem Docker-Setup weitergeleitet werden. Dazu ersetzen Sie die bisherigen Platzhalter-VHosts durch produktive Konfigurationen mit aktiviertem Reverse Proxy.</p><p>Jede Subdomain leitet dabei Anfragen an einen internen Docker-Dienst weiter – OpenCloud, den WOPI-Server oder Collabora. Apache übernimmt die TLS-Terminierung und reicht die Anfrage intern über HTTP oder WebSockets an den richtigen Container weiter.</p><p><strong>Beispiel: OpenCloud (Port 9200) per cloud.blog.opencloud.rocks bereitstellen</strong></p><pre>&lt;IfModule mod_ssl.c&gt;
&lt;VirtualHost *:443&gt;
    ServerName cloud.blog.opencloud.rocks

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/cloud.blog.opencloud.rocks/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/cloud.blog.opencloud.rocks/privkey.pem

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:9200/
    ProxyPassReverse / http://127.0.0.1:9200/

    ErrorLog ${APACHE_LOG_DIR}/cloud_error.log
    CustomLog ${APACHE_LOG_DIR}/cloud_access.log combined
&lt;/VirtualHost&gt;
&lt;/IfModule&gt;
</pre><p><strong>Beispiel: WOPI-Server (Port 9300) per wopiserver.blog.opencloud.rocks anbinden</strong></p><pre>&lt;IfModule mod_ssl.c&gt;
&lt;VirtualHost *:443&gt;
    ServerName wopiserver.blog.opencloud.rocks

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/cloud.blog.opencloud.rocks/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/cloud.blog.opencloud.rocks/privkey.pem

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:9300/
    ProxyPassReverse / http://127.0.0.1:9300/

    ErrorLog ${APACHE_LOG_DIR}/wopi_error.log
    CustomLog ${APACHE_LOG_DIR}/wopi_access.log combined
&lt;/VirtualHost&gt;
&lt;/IfModule&gt;
</pre><p><strong>Collabora (Port 9980): WebSockets, Header und viele Stolperfallen</strong></p><p>Besonderes Augenmerk verdient die Konfiguration für Collabora. Damit die Integration zuverlässig funktioniert – besonders die Office-Vorschau und -Bearbeitung – müssen Sie einige zusätzliche Regeln beachten. Die Herausforderung: Neben klassischen HTTP-Aufrufen nutzt Collabora auch WebSockets, und die müssen explizit durchgereicht werden. So sieht eine funktionierende Konfiguration für collabora.blog.opencloud.rocks aus:</p><pre>&lt;IfModule mod_ssl.c&gt;
&lt;VirtualHost *:443&gt;
    ServerName collabora.blog.opencloud.rocks

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/cloud.blog.opencloud.rocks/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/cloud.blog.opencloud.rocks/privkey.pem

    ProxyPreserveHost On
    AllowEncodedSlashes NoDecode

    # WebSockets
    ProxyPassMatch "/cool/(.*)/ws$" ws://127.0.0.1:9980/cool/$1/ws nocanon
    ProxyPassMatch "^/cool/adminws$" ws://127.0.0.1:9980/cool/adminws

    # Standardpfade
    ProxyPass /cool http://127.0.0.1:9980/cool
    ProxyPassReverse /cool http://127.0.0.1:9980/cool
    ProxyPass /hosting/discovery http://127.0.0.1:9980/hosting/discovery
    ProxyPassReverse /hosting/discovery http://127.0.0.1:9980/hosting/discovery
    ProxyPass /browser http://127.0.0.1:9980/browser
    ProxyPassReverse /browser http://127.0.0.1:9980/browser

    # Wichtiger Header für HTTPS-Verbindung
    RequestHeader set X-Forwarded-Proto "https"

    # Zeitlimits erhöhen
    ProxyTimeout 300
    ProxyIOBufferSize 65536

    ErrorLog ${APACHE_LOG_DIR}/collabora_error.log
    CustomLog ${APACHE_LOG_DIR}/collabora_access.log combined
&lt;/VirtualHost&gt;
&lt;/IfModule&gt;
</pre><p><strong>Apache-Module aktivieren</strong></p><p>Damit das funktioniert, müssen auf dem System auch die nötigen Apache-Module aktiviert sein:&nbsp;</p><pre>$ sudo a2enmod proxy proxy_http ssl headers proxy_connect proxy_wstunnel
[…]
$ systemctl restart apache2</pre><p><strong>Hinweis:&nbsp;</strong>Die zuvor eingerichteten Platzhalter-VHosts (z. B.&nbsp;<code>cloud.blog.opencloud.rocks.conf</code>) dienen ausschließlich dazu, die TLS-Zertifikate mit certbot zu erzeugen. Ändern Sie diese Dateien nicht nachträglich zur produktiven Nutzung! Stattdessen legen Sie eigene Konfigurationsdateien für die HTTPS-VirtualHosts an, die Apache später als Reverse Proxy nutzt. Sobald diese neuen Konfigurationen aktiv sind, können die Platzhalter-VHosts gefahrlos deaktiviert und gelöscht werden.</p><h4>Platzhalter-VHosts jetzt deaktivieren</h4><p>Für die TLS-Zertifikate hatten Sie zuvor einfache Platzhalter-VHosts eingerichtet – jeweils eine Konfiguration pro Subdomain, die lediglich eine statische HTML-Seite ausgeliefert hat. Diese Platzhalter waren notwendig, damit certbot die Domains verifizieren und ein gültiges Zertifikat von Let’s Encrypt ausstellen konnte.</p><p>Jetzt, da Apache produktiv als Reverse Proxy arbeitet und die neuen VHosts aktiv sind, können Sie die alten Konfigurationen entfernen. Andernfalls würde Apache versuchen, mehrere VHosts für dieselbe Subdomain zu laden – das führt zu Fehlermeldungen beim Neustart des Webservers.</p><p>So deaktivieren Sie die überflüssigen Platzhalter-Sites:</p><pre>sudo a2dissite cloud.blog.opencloud.rocks.conf
sudo a2dissite collabora.blog.opencloud.rocks.conf
sudo a2dissite wopiserver.blog.opencloud.rocks.conf
</pre><p>Anschließend laden Sie Apache neu:</p><pre>systemctl restart apache2
</pre><p>Damit ist der Weg frei für das eigentliche OpenCloud-System – erreichbar über die eingerichteten Subdomains mit gültigem TLS-Zertifikat und sicherem Proxy-Zugriff.</p><h4>Docker installieren: Die Grundlage für OpenCloud</h4><p>Bevor Sie OpenCloud auf Ihrem Server starten können, sollten ein paar Voraussetzungen erfüllt sein: Docker und Docker Compose (Version 2) müssen installiert sein, Ihre Domain muss auf den Server zeigen, und Sie sollten sich grundsätzlich mit dem Konzept von Docker Compose auskennen. Klingt kompliziert? Ist es nicht – und Sie müssen auch kein Profi sein, um loszulegen.</p><p><strong>Besonders wichtig:</strong> Achten Sie unbedingt darauf, Docker Compose in Version 2 zu verwenden. In einigen Linux-Distributionen – etwa Debian 12 „Bookworm“ – ist in den Standardpaketen noch die veraltete Version 1 enthalten. Damit funktioniert OpenCloud nicht zuverlässig.</p><p>Die sicherste Methode: Installieren Sie Docker direkt nach der <a href="https://docs.docker.com/engine/install/">offiziellen Anleitung</a>. Damit stellen Sie sicher, dass alle Komponenten aktuell sind – einschließlich docker compose, das später alle Dienste gemeinsam startet und verwaltet. Ob Docker korrekt eingerichtet ist, prüfen Sie einfach mit diesem Befehl:</p><pre>sudo docker run hello-world
</pre><img src="./opencloud_files/docker-hello-world.png" alt="sudo docker run hello-world" width="613" height="418"><p><br>&nbsp;<br><strong>Tipp:</strong> Wenn Sie möchten, dass Ihr normaler Benutzer Docker-Befehle ohne sudo ausführen darf, fügen Sie ihn zur Docker-Gruppe hinzu:</p><pre>sudo usermod -aG docker $USER</pre><p>Nach dem nächsten Login ist die Änderung aktiv – und Ihrem OpenCloud-Setup steht nichts mehr im Weg.</p><h4>OpenCloud vorbereiten: Repository klonen und Konfiguration einrichten</h4><p>Damit Ihr OpenCloud-Setup reibungslos startet, klonen Sie im ersten Schritt das offizielle Compose-Repository und passen anschließend die Konfiguration an Ihre Umgebung an.</p><p>Wechseln Sie in ein geeignetes Verzeichnis und führen Sie folgende Befehle aus:</p><pre>git clone https://github.com/opencloud-eu/opencloud-compose.git
cd opencloud-compose
</pre><p>Erstellen Sie nun auf Basis der mitgelieferten Vorlage Ihre persönliche Umgebungsdatei:</p><pre>cp .env.example .env
</pre><p>Öffnen Sie die Datei .env mit einem Texteditor und tragen Sie dort die folgenden Parameter ein:</p><pre># Domain, unter der OpenCloud später erreichbar sein soll
OC_DOMAIN=cloud.blog.opencloud.rocks

# Admin-Passwort für den ersten Login (Benutzername: admin)
INITIAL_ADMIN_PASSWORD=&lt;top-secret&gt;

# Subdomains für Weboffice und WOPI-Dienst
COLLABORA_DOMAIN=collabora.blog.opencloud.rocks
WOPISERVER_DOMAIN=wopiserver.blog.opencloud.rocks

</pre><p><strong>Tipp:</strong> Zum Generieren eines sicheren Passwortes können Sie das Tool pwgen auf der Kommandozeile verwenden:</p><pre>$ pwgen -cny 12 1
aij)aeSh8mai
</pre><p>Die Optionen -cny sorgen dafür, dass das generierte Passwort mindestens einen Großbuchstaben (-c), eine Zahl (-n) und ein Sonderzeichen (-y) enthält.</p><h4>Dienste auswählen: Welche OpenCloud-Komponenten sollen starten?</h4><p>OpenCloud setzt auf Docker Compose – und erlaubt es Ihnen, gezielt auszuwählen, welche Komponenten Sie wirklich benötigen. Die zentrale Variable in der .env-Datei dafür heißt COMPOSE_FILE. Sie legt fest, welche Dienste beim Start von Docker Compose berücksichtigt werden.</p><p>Für das Setup mit Apache als Reverse Proxy und der Online-Bearbeitung von Dokumenten mit Collabora tragen Sie Folgendes ein:</p><pre>COMPOSE_FILE=docker-compose.yml:weboffice/collabora.yml:external-proxy/opencloud.yml:external-proxy/collabora.yml
</pre><p>Diese Auswahl startet:</p><ul><li><strong>OpenCloud</strong>: die zentrale Plattform</li><li><strong>Collabora Online</strong>: für die Bearbeitung von Office-Dokumenten direkt im Browser</li><li><strong>Apache-spezifische Proxy-Konfigurationen</strong>: damit OpenCloud und Collabora sauber hinter Ihrem Reverse Proxy laufen</li></ul><p>Damit ist Ihr Setup vollständig vorbereitet: Sie kombinieren volle Kontrolle über TLS und Routing mit der vollen Funktionalität von OpenCloud. Im nächsten Schritt starten Sie die Container – und melden sich zum ersten Mal an.</p><h4>OpenCloud starten: Container hochfahren und prüfen</h4><p>Jetzt wird’s konkret: Sie haben die .env-Datei eingerichtet, Apache als Reverse Proxy vorbereitet und alle gewünschten Dienste über COMPOSE_FILE ausgewählt. Nun ist es an der Zeit, OpenCloud zu starten.</p><p>Zuerst laden Sie alle benötigten Container-Images herunter:</p><pre>docker compose pull
</pre><img src="./opencloud_files/docker-compose-pull.png" alt="docker compose pull" width="614" height="341"><p>Dieser Befehl sorgt dafür, dass Docker alle Images für Ihr Setup lokal bereithält – darunter OpenCloud selbst, Collabora für die Bearbeitung von Office-Dokumenten und die zugehörigen Datenbanken.</p><p>Anschließend starten Sie alle konfigurierten Dienste im Hintergrund:</p><pre>docker compose up -d</pre><p><br>Das -d steht für „detached mode“: Die Container laufen im Hintergrund weiter – auch wenn Sie das Terminal schließen.</p><p>Ein kurzer Blick mit docker ps zeigt, ob alles wie geplant läuft:</p><img src="./opencloud_files/docker-ps.png" alt="Docker ps" width="630" height="165"><p>In der Liste der laufenden Container sollten Sie unter anderem opencloud und collabora sehen. Sobald alles gestartet ist, können Sie die Weboberfläche von OpenCloud im Browser aufrufen – unter der Domain, die Sie in der .env-Datei gesetzt haben.</p><h4>OpenCloud im Browser aufrufen</h4><p>Sobald alle Container laufen, öffnen Sie Ihren Browser und rufen die konfigurierte Subdomain auf.</p><img src="./opencloud_files/login-browser-DE_1.png" alt="OpenCloud Login" width="613" height="400"><p><br>Sie sollten nun die Anmeldeseite von OpenCloud sehen. Für den ersten Login verwenden Sie den Benutzernamen admin und das Passwort, das Sie zuvor in der .env unter INITIAL_ADMIN_PASSWORD definiert haben.</p><p><strong>Hinweis:</strong> Nach dem Einloggen sollten Sie das Passwort direkt ändern.</p><p>Wenn alles funktioniert, ist Ihre eigene OpenCloud-Instanz betriebsbereit – sicher per HTTPS erreichbar und eingebunden in Ihre bestehende Infrastruktur.</p><h4>Storage nicht vergessen: OpenCloud-Daten dauerhaft speichern</h4><p>Für den produktiven Betrieb von OpenCloud reicht es nicht, wenn der Login funktioniert – Ihre Daten und Einstellungen müssen auch nach einem Neustart erhalten bleiben. Ohne eigene Speicherpfade landen sie sonst in anonymen Docker-Volumes, die sich nur schwer sichern und kaum verwalten lassen. Für eine saubere und zuverlässige Datenhaltung ist deshalb ein eigenes Verzeichnis außerhalb des Containers empfehlenswert.</p><p>Ein möglicher Ort dafür ist /srv/opencloud. Laut Filesystem Hierarchy Standard (FHS) steht /srv für „Data for services provided by the system“ – also genau das, was OpenCloud tut. Während Pfade wie /opt oder /var/lib eher für Drittsoftware oder temporäre Laufzeitdaten gedacht sind, bietet /srv eine klare Trennung, ist konsistent nutzbar und lässt sich einfach sichern oder in Backups einbinden. Auch /home ist nicht ideal, da dort typischerweise nur Benutzerdaten liegen – nicht die Dienste selbst. Wer ein eigenes Datenlaufwerk eingebunden hat, kann alternativ auch /mnt/opencloud o.&nbsp;Ä. nutzen.</p><p>Im ersten Schritt erstellen Sie die benötigten Verzeichnisse für Konfiguration, Daten und Erweiterungen:</p><pre>mkdir -p /srv/opencloud/{config,data,apps}
chown -R 1000:1000 /srv/opencloud
</pre><p>Der Benutzer mit der UID 1000 ist der Standard-User innerhalb des Containers. Damit OpenCloud auf die neuen Pfade zugreifen kann, muss der Account Besitzer der Verzeichnisse sein. Die Struktur sieht also so aus:</p><pre>/srv/opencloud/
├── config/   → Konfig-Dateien von OpenCloud
├── data/     → Benutzerdaten, Dateien, Inhalte
└── apps/     → ggf. lokale Web-Erweiterungen
</pre><p>Anschließend tragen Sie die neuen Speicherorte in Ihrer .env ein:</p><pre># OpenCloud Speicherorte für Konfiguration, Daten und Apps (lokale Erweiterungen)

# Konfigurationsverzeichnis – persistent, z. B. config.php, Web-Einstellungen usw.
OC_CONFIG_DIR=/srv/opencloud/config

# Datenverzeichnis – hier landen die Dateien der Nutzer*innen
OC_DATA_DIR=/srv/opencloud/data

# Apps-Verzeichnis – für manuell installierte Erweiterungen (optional)
OC_APPS_DIR=/srv/opencloud/apps
</pre><p>Dann stoppen Sie die laufenden Dienste und starten sie mit der angepassten Konfiguration neu:</p><pre>docker compose down
docker compose up -d
</pre><p>Jetzt verwendet OpenCloud die persistenten Verzeichnisse auf Ihrem Server – updatefest, sicher und transparent.</p><p>Ob alles korrekt eingerichtet ist, prüfen Sie mit einem Blick ins laufende Setup:</p><pre>docker inspect opencloud-compose-opencloud-1 | grep /srv/opencloud
ls -l /srv/opencloud/config
</pre><p>Wenn die Datei config.php neu angelegt wurde, ist Ihre Konfiguration erfolgreich – OpenCloud speichert nun dauerhaft alle Daten außerhalb des Containers. Ein wichtiger Schritt für alle, die ihre Instanz langfristig stabil betreiben möchten.</p><img src="./opencloud_files/external_storage.png" alt="External Storage" width="614" height="276"><h4>OpenCloud auf eigenem Server – flexibel, sicher, souverän</h4><p>Mit wenigen gezielten Schritten bringen Sie OpenCloud auf einem eigenen Server zum Laufen – inklusive Reverse Proxy, TLS-Verschlüsselung und dauerhaftem Speicher. Das Ergebnis: Eine voll funktionsfähige Cloud-Plattform, die sich nahtlos in Ihre Infrastruktur integriert, ohne Abhängigkeit von externen Anbietern. Ob im Unternehmen, in der Schule oder privat – mit OpenCloud behalten Sie die Kontrolle über Ihre Daten und bleiben technisch unabhängig.</p>

    </div>
        
      </div>
</section>

</div>

  </div>
  </div>

  </div>

      <div class="sheet__footer">
      <div class="sheet__footer-wrap">
        <div class="sheet__footer-top">
          
        </div>

        <div class="sheet__footer-bottom">
          <div class="sheet__footer-wrapper">
            <div class="sheet__footer-left">
              


              <div class="footer-menu footer-menu--root">
              <div class="footer-menu__item">
        <nav class="footer-menu" aria-label="Footer Navigation">
        <h4 class="footer-menu__title">Über uns</h4>
        
                              <a class="footer-menu__link" href="https://opencloud.eu/de/ueber-uns/unternehmen">Unternehmen</a>
                      <a class="footer-menu__link" href="https://opencloud.eu/de/ueber-uns/karriere-jobs">Karriere / Jobs</a>
                      <a class="footer-menu__link" href="https://opencloud.eu/de/ueber-uns/partner">Partner</a>
                      <a class="footer-menu__link" href="https://opencloud.eu/de/ueber-uns/presse">Presse</a>
                      <a class="footer-menu__link" href="https://opencloud.eu/de/kontakt">Kontakt</a>
                  
        </nav>

      </div>
          <div class="footer-menu__item">
        <nav class="footer-menu" aria-label="Footer Navigation">
        <h4 class="footer-menu__title">Lösungen</h4>
        
                              <a class="footer-menu__link" href="https://opencloud.eu/de/loesungen/oeffentlicher-sektor">Öffentlicher Sektor</a>
                      <a class="footer-menu__link" href="https://opencloud.eu/de/loesungen/forschung-wissenschaft">Forschung &amp; Wissenschaft</a>
                      <a class="footer-menu__link" href="https://opencloud.eu/de/loesungen/bildung">Bildung</a>
                      <a class="footer-menu__link" href="https://opencloud.eu/de/loesungen/unternehmen">Unternehmen</a>
                      <a class="footer-menu__link" href="https://opencloud.eu/de/loesungen/sicherheit">Sicherheit</a>
                      <a class="footer-menu__link" href="https://opencloud.eu/de/loesungen/provider">Provider</a>
                  
        </nav>

      </div>
          <div class="footer-menu__item">
        <nav class="footer-menu" aria-label="Footer Navigation">
        <h4 class="footer-menu__title">Ressourcen</h4>
        
                              <a class="footer-menu__link" href="https://opencloud.eu/de/aktuelles">Blog &amp; News</a>
                      <a class="footer-menu__link" href="https://docs.opencloud.eu/">Dokumentation</a>
                      <a class="footer-menu__link" href="https://opencloud.eu/de/wissenswertes">Wissenswertes</a>
                  
        </nav>

      </div>
          <div class="footer-menu__item">
        <nav class="footer-menu" aria-label="Footer Navigation">
        <h4 class="footer-menu__title">Community</h4>
        
                              <a class="footer-menu__link" href="https://opencloud.eu/de/opencloud-community">OpenCloud Community</a>
                  
        </nav>

      </div>
        
        </div>
    
  



            </div>
            <div class="sheet__footer-right">
              

<div class="language-switcher-language-url lang-switch" id="block-cloudy-sprachumschalter" role="navigation">
  
  <h4 class="lang-switch__title">Sprache:</h4>
  <div class="lang-switch__links">
          <a href="https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server" class="language-link active lang-switch__link">DE</a>
          <a href="https://opencloud.eu/en/install-opencloud-simply-your-own-server" class="language-link lang-switch__link">EN</a>
      </div>
</div>


            </div>
          </div>
        </div>

        <hr class="sheet__footer-spacer">

        <div class="sheet__footer-extended">
          <div class="sheet__footer-icons">
              


<div class="icon-list icon-list--smallspacing">
      <a class="icon-list__item" name="Github Link" target="_blank" href="https://github.com/opencloud-eu">🐱︎</a>
  
      <a class="icon-list__item" name="Linkedin Link" target="_blank" href="https://www.linkedin.com/company/opencloud-eu"></a>
  
      <a class="icon-list__item" name="Mastodon Link" rel="me" target="_blank" href="https://social.opencloud.eu/@OpenCloud">🦣︎</a>
  
      <a class="icon-list__item" name="Bluesky Link" target="_blank" href="https://bsky.app/profile/opencloud.eu">🦋︎</a>
  
    
  
  
      <a class="icon-list__item" name="RSS Link" target="_blank" href="https://opencloud.eu/de/rss.xml" title="News / Blog">📡︎</a>
  
  </div>

            </div>
          <div class="sheet__footer-meta">
            




        <nav class="link-list link-list--footer">
          <a class="link-list__link" href="https://opencloud.eu/de/impressum">Impressum</a>
          <a class="link-list__link" href="https://opencloud.eu/de/datenschutzhinweise">Datenschutz</a>
          <a class="link-list__link" href="https://www.heinlein-support.de/agb">AGB</a>
          <a class="link-list__link" href="https://opencloud.eu/de/erklaerung-zur-barrierefreiheit">Erklärung Barrierefreiheit</a>
          <a class="link-list__link" href="http://opencloud.eu/releasenotes">Release Notes</a>
        </nav>
  



            <div class="sheet__footer-logo">
              © 2026 OpenCloud
            </div>
            <div class="sheet__footer-group-logo">
              <img class="sheet__group-logo" src="./opencloud_files/Hei_Gruppe_Logo_Grau_RGB.svg" alt="Heinlein Group Logo">
            </div>
          </div>
        </div>
      </div>
    </div>
  
</div>

  </div>

    
    <script type="application/json" data-drupal-selector="drupal-settings-json">{"path":{"baseUrl":"\/","pathPrefix":"de\/","currentPath":"node\/2176","currentPathIsAdmin":false,"isFront":false,"currentLanguage":"de"},"pluralDelimiter":"\u0003","suppressDeprecationErrors":true,"ajaxPageState":{"libraries":"eJx1kGEOwyAIhS9U65EWalk1VTCCa3r7uS26dMn-Pb4H5IGLXNfTLuB2s1RVpsl1JDj0xbkzKxaTkGpHHmGFgtDr4Jh-9r1RDKIdRKDNyBHU-YEC7deeph8Bj1Hzxl0nII0jYsINLpHEI7Y9XNA6TpkJSWX-mMZwAfca_mNLghjbjZLBoUxJk90R862JKUOBrUD2YtdSM8T5S-ZKuS4ttcd1klMU0_uRT17jirY","theme":"cloudy","theme_token":null},"ajaxTrustedUrl":[],"csp":{"nonce":"IupZtjp7QXAOtUqDQghgeA"},"user":{"uid":0,"permissionsHash":"13ef9313065cdc959e40f90a6830caa59285a70bd913e48e9eebf1849bc59918"}}</script>
<script src="./opencloud_files/jquery.min.js.Download"></script>
<script src="./opencloud_files/once.min.js.Download"></script>
<script src="./opencloud_files/de_o5dEhAP6o9yx_d-oyPbQqzbfdw-XhQwNFj11GHt9zOo.js.Download"></script>
<script src="./opencloud_files/c9d3346ca20f2076f07f97c755a39833.min.js.Download"></script>
<script src="./opencloud_files/d4593c15c2bd022cfb1e7997e743b756.min.js.Download"></script>
<script src="./opencloud_files/6739dd9d2e1c3205a4de81e528af3ee8.min.js.Download"></script>
<script src="./opencloud_files/index.umd.min.js.Download"></script>
<script src="./opencloud_files/ca7102d2a0283824ce7861a0884ca0fc.min.js.Download"></script>
<script src="./opencloud_files/loadjs.min.js.Download"></script>
<script src="./opencloud_files/408b3e82f72d4c9c910cecc336c7f1f0.min.js.Download"></script>
<script src="./opencloud_files/a02644acdce91883ddb9927e7fc12ca0.min.js.Download"></script>
<script src="./opencloud_files/6c78055ad36c909623049fbdea3ef16f.min.js.Download"></script>
<script src="./opencloud_files/51befca80721239d61efe93b07ca34f9.min.js.Download"></script>
<script src="./opencloud_files/49e6578e81c1b647653880fd458db9ec.min.js.Download"></script>
<script src="./opencloud_files/5c4211fb6c6e9697cc483c350561566b.min.js.Download"></script>
<script src="./opencloud_files/7a5b87abcc907ecc907bd58465de90e8.min.js.Download"></script>
<script src="./opencloud_files/628741c6356d4c3e52b5d22479a95211.min.js.Download"></script>
<script src="./opencloud_files/e28ad0029374459daab8ce0344ff7f44.min.js.Download"></script>
<script src="./opencloud_files/ae246d61d3cf26dce607c6bd059cc6cd.min.js.Download"></script>

  

<script>!function(){const n=[15,60,120];let e=0,i=Date.now(),t=null,o=null,a=document.hasFocus(),l=!1,d=!1;function u(){o=o||setInterval(()=>{e++,n.includes(e)&&d&&c("Time on Page","Time on Page "+e+" Sekunden")},1e3)}function c(n,e,i=null){const t=["trackEvent",n,e,window.location.pathname];null!==i&&t.push(i),window._paq.push(t)}function s(){a&&(a=!1,o&&(clearInterval(o),o=null),t=Date.now())}function r(){var n;a||(a=!0,u(),n=Date.now(),t&&18e5<=n-t&&(window._paq.push(["trackPageView"]),setTimeout(()=>c("Seiteninteraktion","Focus Revisit nach 30+ Minuten"),500),e=0),t=null,i=n)}document.addEventListener("visibilitychange",()=>{"hidden"===document.visibilityState?s():"visible"===document.visibilityState&&r()}),window.addEventListener("blur",()=>{s()}),window.addEventListener("focus",()=>{r()}),window.addEventListener("scroll",function(){var n=window.innerHeight,e=window.scrollY;!l&&n<=e&&(l=!0,c("Seiteninteraktion","Scrolltiefe 1VH")),!d&&50<e&&(d=!0)}),window.addEventListener("beforeprint",function(){c("Seiteninteraktion","Seite drucken")}),"visible"===document.visibilityState&&u()}();</script><div id="drupal-live-announce" class="visually-hidden" aria-live="polite" aria-busy="false"></div><browser-mcp-container data-wxt-shadow-root=""><template shadowrootmode="open">
<!-- saved from url=(0082)https://opencloud.eu/de/opencloud-installieren-ganz-einfach-auf-dem-eigenen-server -->
<html><head><style>/*! tailwindcss v4.0.17 | MIT License | https://tailwindcss.com */@layer theme{:host,:host{--font-sans:ui-sans-serif,system-ui,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";--font-mono:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;--color-red-700:oklch(.505 .213 27.518);--color-blue-300:oklch(.809 .105 251.813);--color-blue-700:oklch(.488 .243 264.376);--color-gray-50:oklch(.985 .002 247.839);--color-gray-100:oklch(.967 .003 264.542);--color-gray-300:oklch(.872 .01 258.338);--color-gray-400:oklch(.707 .022 261.325);--color-gray-500:oklch(.551 .027 264.364);--color-gray-700:oklch(.373 .034 259.733);--color-gray-800:oklch(.278 .033 256.848);--color-gray-900:oklch(.21 .034 264.665);--color-black:#000;--color-white:#fff;--spacing:4px;--container-lg:512px;--text-xs:12px;--text-xs--line-height:calc(1/.75);--text-sm:14px;--text-sm--line-height:calc(1.25/.875);--text-base:16px;--text-base--line-height: 1.5 ;--text-lg:18px;--text-lg--line-height:calc(1.75/1.125);--font-weight-medium:500;--font-weight-semibold:600;--tracking-tight:-.025em;--tracking-widest:.1em;--leading-relaxed:1.625;--radius-xs:2px;--ease-in:cubic-bezier(.4,0,1,1);--animate-spin:spin 1s linear infinite;--animate-pulse:pulse 2s cubic-bezier(.4,0,.6,1)infinite;--default-transition-duration:.15s;--default-transition-timing-function:cubic-bezier(.4,0,.2,1)}}@layer base{*,:after,:before,::backdrop{box-sizing:border-box;border:0 solid;margin:0;padding:0}::file-selector-button{box-sizing:border-box;border:0 solid;margin:0;padding:0}html,:host{-webkit-text-size-adjust:100%;-moz-tab-size:4;tab-size:4;font-feature-settings:initial;font-variation-settings:initial;-webkit-tap-highlight-color:transparent;font-family:ui-sans-serif,system-ui,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;line-height:1.5}hr{height:0;color:inherit;border-top-width:1px}abbr:where([title]){-webkit-text-decoration:underline dotted;text-decoration:underline dotted}h1,h2,h3,h4,h5,h6{font-size:inherit;font-weight:inherit}a{color:inherit;-webkit-text-decoration:inherit;text-decoration:inherit}b,strong{font-weight:bolder}code,kbd,samp,pre{font-feature-settings:initial;font-variation-settings:initial;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;font-size:1em}small{font-size:80%}sub,sup{vertical-align:baseline;font-size:75%;line-height:0;position:relative}sub{bottom:-.25em}sup{top:-.5em}table{text-indent:0;border-color:inherit;border-collapse:collapse}:-moz-focusring{outline:auto}progress{vertical-align:baseline}summary{display:list-item}ol,ul,menu{list-style:none}img,svg,video,canvas,audio,iframe,embed,object{vertical-align:middle;display:block}img,video{max-width:100%;height:auto}button,input,select,optgroup,textarea{font:inherit;font-feature-settings:inherit;font-variation-settings:inherit;letter-spacing:inherit;color:inherit;opacity:1;background-color:#0000;border-radius:0}::file-selector-button{font:inherit;font-feature-settings:inherit;font-variation-settings:inherit;letter-spacing:inherit;color:inherit;opacity:1;background-color:#0000;border-radius:0}:where(select:is([multiple],[size])) optgroup{font-weight:bolder}:where(select:is([multiple],[size])) optgroup option{padding-inline-start:20px}::file-selector-button{margin-inline-end:4px}::placeholder{opacity:1}@supports (not ((-webkit-appearance:-apple-pay-button))) or (contain-intrinsic-size:1px){::placeholder{color:color-mix(in oklab,currentColor 50%,transparent)}}textarea{resize:vertical}::-webkit-search-decoration{-webkit-appearance:none}::-webkit-date-and-time-value{min-height:1lh;text-align:inherit}::-webkit-datetime-edit{padding-block:0}::-webkit-datetime-edit-year-field{padding-block:0}::-webkit-datetime-edit-month-field{padding-block:0}::-webkit-datetime-edit-day-field{padding-block:0}::-webkit-datetime-edit-hour-field{padding-block:0}::-webkit-datetime-edit-minute-field{padding-block:0}::-webkit-datetime-edit-second-field{padding-block:0}::-webkit-datetime-edit-millisecond-field{padding-block:0}::-webkit-datetime-edit-meridiem-field{padding-block:0}:-moz-ui-invalid{box-shadow:none}button,input:where([type=button],[type=reset],[type=submit]){-webkit-appearance:button;-moz-appearance:button;appearance:button}::file-selector-button{-webkit-appearance:button;-moz-appearance:button;appearance:button}::-webkit-inner-spin-button{height:auto}::-webkit-outer-spin-button{height:auto}[hidden]:where(:not([hidden=until-found])){display:none!important}*{border-color:var(--border);outline-color:color-mix(in oklab,var(--ring)50%,transparent)}body{background-color:var(--background);color:var(--foreground)}button:not(:disabled),[role=button]:not(:disabled){cursor:pointer}:host{all:initial!important;font-family:var(--font-sans)!important;font-size:var(--text-base)!important;line-height:var(--tw-leading,var(--text-base--line-height))!important}:host,:host *{border-color:var(--border)}:host{background-color:var(--background)!important;color:var(--foreground)!important}[type=text],input:where(:not([type])),[type=email],[type=url],[type=password],[type=number],[type=date],[type=datetime-local],[type=month],[type=search],[type=tel],[type=time],[type=week],[multiple],textarea,select{-webkit-appearance:none;-moz-appearance:none;appearance:none;border-color:#6a7282;--tw-shadow:0 0 #0000;background-color:#fff;border-width:1px;border-radius:0;padding:8px 12px;font-size:16px;line-height:24px}:is([type=text],input:where(:not([type])),[type=email],[type=url],[type=password],[type=number],[type=date],[type=datetime-local],[type=month],[type=search],[type=tel],[type=time],[type=week],[multiple],textarea,select):focus{outline-offset:2px;--tw-ring-inset:var(--tw-empty, );--tw-ring-offset-width:0px;--tw-ring-offset-color:#fff;--tw-ring-color:oklch(.546 .245 262.881);--tw-ring-offset-shadow:var(--tw-ring-inset)0 0 0 var(--tw-ring-offset-width)var(--tw-ring-offset-color);--tw-ring-shadow:var(--tw-ring-inset)0 0 0 calc(1px + var(--tw-ring-offset-width))var(--tw-ring-color);box-shadow:var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow);border-color:#155dfc;outline:2px solid #0000}input::placeholder,textarea::placeholder{color:#6a7282;opacity:1}::-webkit-datetime-edit-fields-wrapper{padding:0}::-webkit-date-and-time-value{min-height:1.5em}::-webkit-date-and-time-value{text-align:inherit}::-webkit-datetime-edit{display:inline-flex}::-webkit-datetime-edit{padding-top:0;padding-bottom:0}::-webkit-datetime-edit-year-field{padding-top:0;padding-bottom:0}::-webkit-datetime-edit-month-field{padding-top:0;padding-bottom:0}::-webkit-datetime-edit-day-field{padding-top:0;padding-bottom:0}::-webkit-datetime-edit-hour-field{padding-top:0;padding-bottom:0}::-webkit-datetime-edit-minute-field{padding-top:0;padding-bottom:0}::-webkit-datetime-edit-second-field{padding-top:0;padding-bottom:0}::-webkit-datetime-edit-millisecond-field{padding-top:0;padding-bottom:0}::-webkit-datetime-edit-meridiem-field{padding-top:0;padding-bottom:0}select{-webkit-print-color-adjust:exact;print-color-adjust:exact;background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='oklch(0.551 0.027 264.364)' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e");background-position:right 8px center;background-repeat:no-repeat;background-size:1.5em 1.5em;padding-right:40px}[multiple],[size]:where(select:not([size="1"])){background-image:initial;background-position:initial;background-repeat:unset;background-size:initial;-webkit-print-color-adjust:unset;print-color-adjust:unset;padding-right:12px}[type=checkbox],[type=radio]{-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-print-color-adjust:exact;print-color-adjust:exact;vertical-align:middle;-webkit-user-select:none;user-select:none;width:16px;height:16px;color:#155dfc;border-color:#6a7282;--tw-shadow:0 0 #0000;background-color:#fff;background-origin:border-box;border-width:1px;flex-shrink:0;padding:0;display:inline-block}[type=checkbox]{border-radius:0}[type=radio]{border-radius:100%}[type=checkbox]:focus,[type=radio]:focus{outline-offset:2px;--tw-ring-inset:var(--tw-empty, );--tw-ring-offset-width:2px;--tw-ring-offset-color:#fff;--tw-ring-color:oklch(.546 .245 262.881);--tw-ring-offset-shadow:var(--tw-ring-inset)0 0 0 var(--tw-ring-offset-width)var(--tw-ring-offset-color);--tw-ring-shadow:var(--tw-ring-inset)0 0 0 calc(2px + var(--tw-ring-offset-width))var(--tw-ring-color);box-shadow:var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow);outline:2px solid #0000}[type=checkbox]:checked,[type=radio]:checked{background-color:currentColor;background-position:50%;background-repeat:no-repeat;background-size:100% 100%;border-color:#0000}[type=checkbox]:checked{background-image:url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.207 4.793a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-2-2a1 1 0 011.414-1.414L6.5 9.086l4.293-4.293a1 1 0 011.414 0z'/%3e%3c/svg%3e")}@media (forced-colors:active){[type=checkbox]:checked{-webkit-appearance:auto;-moz-appearance:auto;appearance:auto}}[type=radio]:checked{background-image:url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3ccircle cx='8' cy='8' r='3'/%3e%3c/svg%3e")}@media (forced-colors:active){[type=radio]:checked{-webkit-appearance:auto;-moz-appearance:auto;appearance:auto}}[type=checkbox]:checked:hover,[type=checkbox]:checked:focus,[type=radio]:checked:hover,[type=radio]:checked:focus{background-color:currentColor;border-color:#0000}[type=checkbox]:indeterminate{background-color:currentColor;background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 16 16'%3e%3cpath stroke='white' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M4 8h8'/%3e%3c/svg%3e");background-position:50%;background-repeat:no-repeat;background-size:100% 100%;border-color:#0000}@media (forced-colors:active){[type=checkbox]:indeterminate{-webkit-appearance:auto;-moz-appearance:auto;appearance:auto}}[type=checkbox]:indeterminate:hover,[type=checkbox]:indeterminate:focus{background-color:currentColor;border-color:#0000}[type=file]{background:unset;border-color:inherit;font-size:unset;line-height:inherit;border-width:0;border-radius:0;padding:0}[type=file]:focus{outline:1px solid buttontext;outline:1px auto -webkit-focus-ring-color}}@layer components;@layer utilities{.pointer-events-none{pointer-events:none}.visible{visibility:visible}.sr-only{clip:rect(0,0,0,0);white-space:nowrap;border-width:0;width:1px;height:1px;margin:-1px;padding:0;position:absolute;overflow:hidden}.absolute{position:absolute}.fixed{position:fixed}.relative{position:relative}.static{position:static}.sticky{position:sticky}.inset-0{inset:calc(var(--spacing)*0)}.-top-1{top:calc(var(--spacing)*-1)}.top-\(--line-offset\){top:var(--line-offset)}.top-\(--terminal-radius\){top:var(--terminal-radius)}.top-0{top:calc(var(--spacing)*0)}.top-2{top:calc(var(--spacing)*2)}.top-4{top:calc(var(--spacing)*4)}.top-\[50\%\]{top:50%}.right-\(--line-offset\){right:var(--line-offset)}.right-0{right:calc(var(--spacing)*0)}.right-2{right:calc(var(--spacing)*2)}.right-4{right:calc(var(--spacing)*4)}.bottom-\(--line-offset\){bottom:var(--line-offset)}.bottom-0{bottom:calc(var(--spacing)*0)}.-left-1{left:calc(var(--spacing)*-1)}.left-\(--line-offset\){left:var(--line-offset)}.left-\(--terminal-radius\){left:var(--terminal-radius)}.left-0{left:calc(var(--spacing)*0)}.left-2{left:calc(var(--spacing)*2)}.left-\[50\%\]{left:50%}.z-10{z-index:10}.z-20{z-index:20}.z-30{z-index:30}.z-50{z-index:50}.z-2147483647{z-index:2147483647}.col-start-2{grid-column-start:2}.container{width:100%}@media (width>=40rem){.container{max-width:640px}}@media (width>=48rem){.container{max-width:768px}}@media (width>=64rem){.container{max-width:1024px}}@media (width>=80rem){.container{max-width:1280px}}@media (width>=96rem){.container{max-width:1536px}}.-mx-1{margin-inline:calc(var(--spacing)*-1)}.mx-4{margin-inline:calc(var(--spacing)*4)}.my-1{margin-block:calc(var(--spacing)*1)}.my-4{margin-block:calc(var(--spacing)*4)}.mt-2{margin-top:calc(var(--spacing)*2)}.mt-4{margin-top:calc(var(--spacing)*4)}.mr-1{margin-right:calc(var(--spacing)*1)}.mr-2{margin-right:calc(var(--spacing)*2)}.mb-0{margin-bottom:calc(var(--spacing)*0)}.ml-auto{margin-left:auto}.box-border{box-sizing:border-box}.line-clamp-1{-webkit-line-clamp:1;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}.block{display:block}.contents{display:contents}.flex{display:flex}.grid{display:grid}.inline{display:inline}.inline-flex{display:inline-flex}.table{display:table}.table-caption{display:table-caption}.table-cell{display:table-cell}.table-row{display:table-row}.field-sizing-content{field-sizing:content}.size-2{width:calc(var(--spacing)*2);height:calc(var(--spacing)*2)}.size-2\.5{width:calc(var(--spacing)*2.5);height:calc(var(--spacing)*2.5)}.size-3\.5{width:calc(var(--spacing)*3.5);height:calc(var(--spacing)*3.5)}.size-4{width:calc(var(--spacing)*4);height:calc(var(--spacing)*4)}.size-5{width:calc(var(--spacing)*5);height:calc(var(--spacing)*5)}.size-6{width:calc(var(--spacing)*6);height:calc(var(--spacing)*6)}.size-8{width:calc(var(--spacing)*8);height:calc(var(--spacing)*8)}.size-9{width:calc(var(--spacing)*9);height:calc(var(--spacing)*9)}.size-full{width:100%;height:100%}.h-\(--line-thickness\){height:var(--line-thickness)}.h-4{height:calc(var(--spacing)*4)}.h-5{height:calc(var(--spacing)*5)}.h-6{height:calc(var(--spacing)*6)}.h-8{height:calc(var(--spacing)*8)}.h-9{height:calc(var(--spacing)*9)}.h-10{height:calc(var(--spacing)*10)}.h-\[22px\]{height:22px}.h-\[var\(--radix-select-trigger-height\)\]{height:var(--radix-select-trigger-height)}.h-full{height:100%}.h-px{height:1px}.h-screen{height:100vh}.max-h-\(--radix-dropdown-menu-content-available-height\){max-height:var(--radix-dropdown-menu-content-available-height)}.max-h-80{max-height:calc(var(--spacing)*80)}.max-h-96{max-height:calc(var(--spacing)*96)}.min-h-4{min-height:calc(var(--spacing)*4)}.min-h-16{min-height:calc(var(--spacing)*16)}.w-\(--line-thickness\){width:var(--line-thickness)}.w-3\/4{width:75%}.w-9{width:calc(var(--spacing)*9)}.w-72{width:calc(var(--spacing)*72)}.w-fit{width:fit-content}.w-full{width:100%}.w-px{width:1px}.max-w-\[calc\(100\%-2rem\)\]{max-width:calc(100% - 32px)}.min-w-0{min-width:calc(var(--spacing)*0)}.min-w-\[8rem\]{min-width:128px}.min-w-\[300px\]{min-width:300px}.min-w-\[var\(--radix-select-trigger-width\)\]{min-width:var(--radix-select-trigger-width)}.flex-1{flex:1}.shrink-0{flex-shrink:0}.grow{flex-grow:1}.caption-bottom{caption-side:bottom}.translate-x-\[-50\%\]{--tw-translate-x:-50%;translate:var(--tw-translate-x)var(--tw-translate-y)}.translate-y-0\.5{--tw-translate-y:calc(var(--spacing)*.5);translate:var(--tw-translate-x)var(--tw-translate-y)}.translate-y-\[-50\%\]{--tw-translate-y:-50%;translate:var(--tw-translate-x)var(--tw-translate-y)}.translate-y-\[calc\(-50\%_-_2px\)\]{--tw-translate-y: calc(-50% - 2px) ;translate:var(--tw-translate-x)var(--tw-translate-y)}.rotate-45{rotate:45deg}.transform{transform:var(--tw-rotate-x)var(--tw-rotate-y)var(--tw-rotate-z)var(--tw-skew-x)var(--tw-skew-y)}.animate-caret-blink{animation:1.25s ease-out infinite caret-blink}.animate-pulse{animation:var(--animate-pulse)}.animate-spin{animation:var(--animate-spin)}.cursor-col-resize{cursor:col-resize}.cursor-default{cursor:default}.resize-none{resize:none}.scroll-my-1{scroll-margin-block:calc(var(--spacing)*1)}.grid-cols-\[0_1fr\]{grid-template-columns:0 1fr}.flex-col{flex-direction:column}.flex-col-reverse{flex-direction:column-reverse}.flex-wrap{flex-wrap:wrap}.items-center{align-items:center}.items-start{align-items:flex-start}.justify-between{justify-content:space-between}.justify-center{justify-content:center}.justify-items-start{justify-items:start}.gap-1{gap:calc(var(--spacing)*1)}.gap-1\.5{gap:calc(var(--spacing)*1.5)}.gap-2{gap:calc(var(--spacing)*2)}.gap-4{gap:calc(var(--spacing)*4)}.gap-6{gap:calc(var(--spacing)*6)}:where(.space-y-1>:not(:last-child)){--tw-space-y-reverse:0;margin-block-start:calc(calc(var(--spacing)*1)*var(--tw-space-y-reverse));margin-block-end:calc(calc(var(--spacing)*1)*calc(1 - var(--tw-space-y-reverse)))}:where(.space-y-2>:not(:last-child)){--tw-space-y-reverse:0;margin-block-start:calc(calc(var(--spacing)*2)*var(--tw-space-y-reverse));margin-block-end:calc(calc(var(--spacing)*2)*calc(1 - var(--tw-space-y-reverse)))}:where(.space-y-4>:not(:last-child)){--tw-space-y-reverse:0;margin-block-start:calc(calc(var(--spacing)*4)*var(--tw-space-y-reverse));margin-block-end:calc(calc(var(--spacing)*4)*calc(1 - var(--tw-space-y-reverse)))}:where(.space-x-0\.5>:not(:last-child)){--tw-space-x-reverse:0;margin-inline-start:calc(calc(var(--spacing)*.5)*var(--tw-space-x-reverse));margin-inline-end:calc(calc(var(--spacing)*.5)*calc(1 - var(--tw-space-x-reverse)))}:where(.space-x-2>:not(:last-child)){--tw-space-x-reverse:0;margin-inline-start:calc(calc(var(--spacing)*2)*var(--tw-space-x-reverse));margin-inline-end:calc(calc(var(--spacing)*2)*calc(1 - var(--tw-space-x-reverse)))}:where(.space-x-4>:not(:last-child)){--tw-space-x-reverse:0;margin-inline-start:calc(calc(var(--spacing)*4)*var(--tw-space-x-reverse));margin-inline-end:calc(calc(var(--spacing)*4)*calc(1 - var(--tw-space-x-reverse)))}.gap-y-0\.5{row-gap:calc(var(--spacing)*.5)}.overflow-auto{overflow:auto}.overflow-hidden{overflow:hidden}.overflow-x-auto{overflow-x:auto}.overflow-x-hidden{overflow-x:hidden}.overflow-y-auto{overflow-y:auto}.rounded-\[2px\]{border-radius:2px}.rounded-\[4px\]{border-radius:4px}.rounded-full{border-radius:3.40282e38px}.rounded-lg{border-radius:var(--radius)}.rounded-md{border-radius:calc(var(--radius) - 2px)}.rounded-sm{border-radius:calc(var(--radius) - 4px)}.rounded-xl{border-radius:calc(var(--radius) + 4px)}.rounded-xs{border-radius:var(--radius-xs)}.border{border-style:var(--tw-border-style);border-width:1px}.border-0{border-style:var(--tw-border-style);border-width:0}.border-2{border-style:var(--tw-border-style);border-width:2px}.border-y{border-block-style:var(--tw-border-style);border-block-width:1px}.border-t{border-top-style:var(--tw-border-style);border-top-width:1px}.border-r{border-right-style:var(--tw-border-style);border-right-width:1px}.border-b{border-bottom-style:var(--tw-border-style);border-bottom-width:1px}.border-l{border-left-style:var(--tw-border-style);border-left-width:1px}.border-gray-300{border-color:var(--color-gray-300)}.border-input{border-color:var(--input)}.border-transparent{border-color:#0000}.bg-background{background-color:var(--background)}.bg-background\/80{background-color:color-mix(in oklab,var(--background)80%,transparent)}.bg-black\/80{background-color:color-mix(in oklab,var(--color-black)80%,transparent)}.bg-blue-700{background-color:var(--color-blue-700)}.bg-border{background-color:var(--border)}.bg-card{background-color:var(--card)}.bg-destructive{background-color:var(--destructive)}.bg-foreground{background-color:var(--foreground)}.bg-gray-50{background-color:var(--color-gray-50)}.bg-gray-100{background-color:var(--color-gray-100)}.bg-gray-500{background-color:var(--color-gray-500)}.bg-gray-700{background-color:var(--color-gray-700)}.bg-muted{background-color:var(--muted)}.bg-muted\/50{background-color:color-mix(in oklab,var(--muted)50%,transparent)}.bg-popover{background-color:var(--popover)}.bg-primary{background-color:var(--primary)}.bg-primary\/10{background-color:color-mix(in oklab,var(--primary)10%,transparent)}.bg-secondary{background-color:var(--secondary)}.bg-transparent{background-color:#0000}.bg-white{background-color:var(--color-white)}.fill-black{fill:var(--color-black)}.fill-current{fill:currentColor}.fill-primary{fill:var(--primary)}.stroke-white{stroke:var(--color-white)}.stroke-\[1\.5\]{stroke-width:1.5px}.p-0{padding:calc(var(--spacing)*0)}.p-0\.5{padding:calc(var(--spacing)*.5)}.p-1{padding:calc(var(--spacing)*1)}.p-1\.5{padding:calc(var(--spacing)*1.5)}.p-2{padding:calc(var(--spacing)*2)}.p-3{padding:calc(var(--spacing)*3)}.p-4{padding:calc(var(--spacing)*4)}.p-6{padding:calc(var(--spacing)*6)}.px-1{padding-inline:calc(var(--spacing)*1)}.px-2{padding-inline:calc(var(--spacing)*2)}.px-3{padding-inline:calc(var(--spacing)*3)}.px-4{padding-inline:calc(var(--spacing)*4)}.px-6{padding-inline:calc(var(--spacing)*6)}.py-0{padding-block:calc(var(--spacing)*0)}.py-0\.5{padding-block:calc(var(--spacing)*.5)}.py-1{padding-block:calc(var(--spacing)*1)}.py-1\.5{padding-block:calc(var(--spacing)*1.5)}.py-2{padding-block:calc(var(--spacing)*2)}.py-3{padding-block:calc(var(--spacing)*3)}.py-4{padding-block:calc(var(--spacing)*4)}.py-6{padding-block:calc(var(--spacing)*6)}.py-\[1px\]{padding-block:1px}.pt-0{padding-top:calc(var(--spacing)*0)}.pt-2{padding-top:calc(var(--spacing)*2)}.pr-2{padding-right:calc(var(--spacing)*2)}.pr-8{padding-right:calc(var(--spacing)*8)}.pb-4{padding-bottom:calc(var(--spacing)*4)}.pl-2{padding-left:calc(var(--spacing)*2)}.pl-8{padding-left:calc(var(--spacing)*8)}.text-center{text-align:center}.text-left{text-align:left}.align-middle{vertical-align:middle}.font-mono{font-family:var(--font-mono)}.text-base{font-size:var(--text-base);line-height:var(--tw-leading,var(--text-base--line-height))}.text-lg{font-size:var(--text-lg);line-height:var(--tw-leading,var(--text-lg--line-height))}.text-sm{font-size:var(--text-sm);line-height:var(--tw-leading,var(--text-sm--line-height))}.text-xs{font-size:var(--text-xs);line-height:var(--tw-leading,var(--text-xs--line-height))}.leading-none{--tw-leading:1;line-height:1}.font-medium{--tw-font-weight:var(--font-weight-medium);font-weight:var(--font-weight-medium)}.font-semibold{--tw-font-weight:var(--font-weight-semibold);font-weight:var(--font-weight-semibold)}.tracking-tight{--tw-tracking:var(--tracking-tight);letter-spacing:var(--tracking-tight)}.tracking-widest{--tw-tracking:var(--tracking-widest);letter-spacing:var(--tracking-widest)}.text-balance{text-wrap:balance}.break-all{word-break:break-all}.whitespace-nowrap{white-space:nowrap}.whitespace-pre-wrap{white-space:pre-wrap}.text-black{color:var(--color-black)}.text-card-foreground{color:var(--card-foreground)}.text-current{color:currentColor}.text-destructive-foreground{color:var(--destructive-foreground)}.text-foreground{color:var(--foreground)}.text-gray-500{color:var(--color-gray-500)}.text-gray-700{color:var(--color-gray-700)}.text-gray-900{color:var(--color-gray-900)}.text-muted-foreground{color:var(--muted-foreground)}.text-popover-foreground{color:var(--popover-foreground)}.text-primary{color:var(--primary)}.text-primary-foreground{color:var(--primary-foreground)}.text-red-700{color:var(--color-red-700)}.text-secondary-foreground{color:var(--secondary-foreground)}.text-white{color:var(--color-white)}.underline-offset-4{text-underline-offset:4px}.opacity-0{opacity:0}.opacity-25{opacity:.25}.opacity-50{opacity:.5}.opacity-70{opacity:.7}.opacity-75{opacity:.75}.shadow-lg{--tw-shadow:0 10px 15px -3px var(--tw-shadow-color,#0000001a),0 4px 6px -4px var(--tw-shadow-color,#0000001a);box-shadow:var(--tw-inset-shadow),var(--tw-inset-ring-shadow),var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow)}.shadow-md{--tw-shadow:0 4px 6px -1px var(--tw-shadow-color,#0000001a),0 2px 4px -2px var(--tw-shadow-color,#0000001a);box-shadow:var(--tw-inset-shadow),var(--tw-inset-ring-shadow),var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow)}.shadow-sm{--tw-shadow:0 1px 3px 0 var(--tw-shadow-color,#0000001a),0 1px 2px -1px var(--tw-shadow-color,#0000001a);box-shadow:var(--tw-inset-shadow),var(--tw-inset-ring-shadow),var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow)}.shadow-xs{--tw-shadow:0 1px 2px 0 var(--tw-shadow-color,#0000000d);box-shadow:var(--tw-inset-shadow),var(--tw-inset-ring-shadow),var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow)}.ring-0{--tw-ring-shadow:var(--tw-ring-inset,)0 0 0 calc(0px + var(--tw-ring-offset-width))var(--tw-ring-color,currentColor);box-shadow:var(--tw-inset-shadow),var(--tw-inset-ring-shadow),var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow)}.ring-1{--tw-ring-shadow:var(--tw-ring-inset,)0 0 0 calc(1px + var(--tw-ring-offset-width))var(--tw-ring-color,currentColor);box-shadow:var(--tw-inset-shadow),var(--tw-inset-ring-shadow),var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow)}.ring-gray-500\/10{--tw-ring-color:color-mix(in oklab,var(--color-gray-500)10%,transparent)}.ring-offset-background{--tw-ring-offset-color:var(--background)}.outline-hidden{--tw-outline-style:none;outline-style:none}@media (forced-colors:active){.outline-hidden{outline-offset:2px;outline:2px solid #0000}}.outline{outline-style:var(--tw-outline-style);outline-width:1px}.transition-\[color\,box-shadow\]{transition-property:color,box-shadow;transition-timing-function:var(--tw-ease,var(--default-transition-timing-function));transition-duration:var(--tw-duration,var(--default-transition-duration))}.transition-all{transition-property:all;transition-timing-function:var(--tw-ease,var(--default-transition-timing-function));transition-duration:var(--tw-duration,var(--default-transition-duration))}.transition-colors{transition-property:color,background-color,border-color,outline-color,text-decoration-color,fill,stroke,--tw-gradient-from,--tw-gradient-via,--tw-gradient-to;transition-timing-function:var(--tw-ease,var(--default-transition-timing-function));transition-duration:var(--tw-duration,var(--default-transition-duration))}.transition-opacity{transition-property:opacity;transition-timing-function:var(--tw-ease,var(--default-transition-timing-function));transition-duration:var(--tw-duration,var(--default-transition-duration))}.transition-shadow{transition-property:box-shadow;transition-timing-function:var(--tw-ease,var(--default-transition-timing-function));transition-duration:var(--tw-duration,var(--default-transition-duration))}.transition-transform{transition-property:transform,translate,scale,rotate;transition-timing-function:var(--tw-ease,var(--default-transition-timing-function));transition-duration:var(--tw-duration,var(--default-transition-duration))}.transition-none{transition-property:none}.duration-200{--tw-duration:.2s;transition-duration:.2s}.duration-500{--tw-duration:.5s;transition-duration:.5s}.duration-1000{--tw-duration:1s;transition-duration:1s}.ease-in{--tw-ease:var(--ease-in);transition-timing-function:var(--ease-in)}.animate-in{--tw-enter-opacity:initial;--tw-enter-scale:initial;--tw-enter-rotate:initial;--tw-enter-translate-x:initial;--tw-enter-translate-y:initial;animation-name:enter;animation-duration:.15s}.outline-none{--tw-outline-style:none;outline-style:none}.select-none{-webkit-user-select:none;user-select:none}.duration-200{animation-duration:.2s}.duration-500{animation-duration:.5s}.duration-1000{animation-duration:1s}.ease-in{animation-timing-function:cubic-bezier(.4,0,1,1)}.fade-in-0{--tw-enter-opacity:0}.ring-inset{--tw-ring-inset:inset}.running{animation-play-state:running}.zoom-in-95{--tw-enter-scale:.95}@media (hover:hover){.group-hover\:opacity-100:is(:where(.group):hover *){opacity:1}}.group-data-\[disabled\=true\]\:pointer-events-none:is(:where(.group)[data-disabled=true] *){pointer-events:none}.group-data-\[disabled\=true\]\:opacity-50:is(:where(.group)[data-disabled=true] *){opacity:.5}.group-\[\.toast\]\:bg-muted:is(:where(.group).toast *){background-color:var(--muted)}.group-\[\.toast\]\:bg-primary:is(:where(.group).toast *){background-color:var(--primary)}.group-\[\.toast\]\:text-muted-foreground:is(:where(.group).toast *){color:var(--muted-foreground)}.group-\[\.toast\]\:text-primary-foreground:is(:where(.group).toast *){color:var(--primary-foreground)}.group-\[\.toaster\]\:border-border:is(:where(.group).toaster *){border-color:var(--border)}.group-\[\.toaster\]\:bg-background:is(:where(.group).toaster *){background-color:var(--background)}.group-\[\.toaster\]\:text-foreground:is(:where(.group).toaster *){color:var(--foreground)}.group-\[\.toaster\]\:shadow-lg:is(:where(.group).toaster *){--tw-shadow:0 10px 15px -3px var(--tw-shadow-color,#0000001a),0 4px 6px -4px var(--tw-shadow-color,#0000001a);box-shadow:var(--tw-inset-shadow),var(--tw-inset-ring-shadow),var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow)}.peer-disabled\:cursor-not-allowed:is(:where(.peer):disabled~*){cursor:not-allowed}.peer-disabled\:opacity-50:is(:where(.peer):disabled~*){opacity:.5}.selection\:bg-primary ::selection{background-color:var(--primary)}.selection\:bg-primary::selection{background-color:var(--primary)}.selection\:text-primary-foreground ::selection{color:var(--primary-foreground)}.selection\:text-primary-foreground::selection{color:var(--primary-foreground)}.file\:inline-flex::file-selector-button{display:inline-flex}.file\:h-7::file-selector-button{height:calc(var(--spacing)*7)}.file\:border-0::file-selector-button{border-style:var(--tw-border-style);border-width:0}.file\:bg-transparent::file-selector-button{background-color:#0000}.file\:text-sm::file-selector-button{font-size:var(--text-sm);line-height:var(--tw-leading,var(--text-sm--line-height))}.file\:font-medium::file-selector-button{--tw-font-weight:var(--font-weight-medium);font-weight:var(--font-weight-medium)}.file\:text-foreground::file-selector-button{color:var(--foreground)}.placeholder\:text-muted-foreground::placeholder{color:var(--muted-foreground)}.before\:absolute:before{content:var(--tw-content);position:absolute}.before\:top-\(--negative-terminal-size\):before{content:var(--tw-content);top:var(--negative-terminal-size)}.before\:top-\(--offset-terminal\):before{content:var(--tw-content);top:var(--offset-terminal)}.before\:right-\(--offset-terminal\):before{content:var(--tw-content);right:var(--offset-terminal)}.before\:bottom-\(--offset-terminal\):before{content:var(--tw-content);bottom:var(--offset-terminal)}.before\:left-\(--negative-terminal-size\):before{content:var(--tw-content);left:var(--negative-terminal-size)}.before\:left-\(--offset-terminal\):before{content:var(--tw-content);left:var(--offset-terminal)}.before\:h-\(--terminal-size\):before{content:var(--tw-content);height:var(--terminal-size)}.before\:w-\(--terminal-size\):before{content:var(--tw-content);width:var(--terminal-size)}.before\:rounded-full:before{content:var(--tw-content);border-radius:3.40282e38px}.before\:border-\(length\:--line-thickness\):before{content:var(--tw-content);border-style:var(--tw-border-style);border-width:var(--line-thickness)}.before\:border-solid:before{content:var(--tw-content);--tw-border-style:solid;border-style:solid}.before\:border-blue-700:before{content:var(--tw-content);border-color:var(--color-blue-700)}.before\:content-\[\'\'\]:before{--tw-content:"";content:var(--tw-content)}.first\:rounded-l-md:first-child{border-top-left-radius:calc(var(--radius) - 2px);border-bottom-left-radius:calc(var(--radius) - 2px)}.first\:border-l:first-child{border-left-style:var(--tw-border-style);border-left-width:1px}.last\:rounded-r-md:last-child{border-top-right-radius:calc(var(--radius) - 2px);border-bottom-right-radius:calc(var(--radius) - 2px)}.last\:border-b-0:last-child{border-bottom-style:var(--tw-border-style);border-bottom-width:0}@media (hover:hover){.hover\:bg-accent:hover{background-color:var(--accent)}.hover\:bg-background:hover{background-color:var(--background)}.hover\:bg-destructive\/90:hover{background-color:color-mix(in oklab,var(--destructive)90%,transparent)}.hover\:bg-gray-500:hover{background-color:var(--color-gray-500)}.hover\:bg-gray-800:hover{background-color:var(--color-gray-800)}.hover\:bg-muted\/50:hover{background-color:color-mix(in oklab,var(--muted)50%,transparent)}.hover\:bg-primary\/90:hover{background-color:color-mix(in oklab,var(--primary)90%,transparent)}.hover\:bg-secondary\/80:hover{background-color:color-mix(in oklab,var(--secondary)80%,transparent)}.hover\:text-accent-foreground:hover{color:var(--accent-foreground)}.hover\:text-gray-400:hover{color:var(--color-gray-400)}.hover\:underline:hover{text-decoration-line:underline}.hover\:opacity-100:hover{opacity:1}}.focus\:bg-accent:focus{background-color:var(--accent)}.focus\:bg-white:focus{background-color:var(--color-white)}.focus\:text-accent-foreground:focus{color:var(--accent-foreground)}.focus\:ring-2:focus{--tw-ring-shadow:var(--tw-ring-inset,)0 0 0 calc(2px + var(--tw-ring-offset-width))var(--tw-ring-color,currentColor);box-shadow:var(--tw-inset-shadow),var(--tw-inset-ring-shadow),var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow)}.focus\:ring-blue-300:focus{--tw-ring-color:var(--color-blue-300)}.focus\:ring-ring:focus{--tw-ring-color:var(--ring)}.focus\:ring-offset-2:focus{--tw-ring-offset-width:2px;--tw-ring-offset-shadow:var(--tw-ring-inset,)0 0 0 var(--tw-ring-offset-width)var(--tw-ring-offset-color)}.focus\:outline-hidden:focus{--tw-outline-style:none;outline-style:none}@media (forced-colors:active){.focus\:outline-hidden:focus{outline-offset:2px;outline:2px solid #0000}}.focus\:ring-inset:focus{--tw-ring-inset:inset}.focus-visible\:border-ring:focus-visible{border-color:var(--ring)}.focus-visible\:ring-\[3px\]:focus-visible{--tw-ring-shadow:var(--tw-ring-inset,)0 0 0 calc(3px + var(--tw-ring-offset-width))var(--tw-ring-color,currentColor);box-shadow:var(--tw-inset-shadow),var(--tw-inset-ring-shadow),var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow)}.focus-visible\:ring-destructive\/20:focus-visible{--tw-ring-color:color-mix(in oklab,var(--destructive)20%,transparent)}.focus-visible\:ring-ring\/50:focus-visible{--tw-ring-color:color-mix(in oklab,var(--ring)50%,transparent)}.focus-visible\:outline-1:focus-visible{outline-style:var(--tw-outline-style);outline-width:1px}.focus-visible\:outline-ring:focus-visible{outline-color:var(--ring)}.disabled\:pointer-events-none:disabled{pointer-events:none}.disabled\:cursor-not-allowed:disabled{cursor:not-allowed}.disabled\:opacity-50:disabled,.has-disabled\:opacity-50:has(:disabled){opacity:.5}.has-\[\>svg\]\:grid-cols-\[calc\(var\(--spacing\)\*4\)_1fr\]:has(>svg){grid-template-columns:calc(var(--spacing)*4)1fr}.has-\[\>svg\]\:gap-x-3:has(>svg){column-gap:calc(var(--spacing)*3)}.has-\[\>svg\]\:px-2\.5:has(>svg){padding-inline:calc(var(--spacing)*2.5)}.has-\[\>svg\]\:px-3:has(>svg){padding-inline:calc(var(--spacing)*3)}.has-\[\>svg\]\:px-4:has(>svg){padding-inline:calc(var(--spacing)*4)}.aria-invalid\:border-destructive[aria-invalid=true]{border-color:var(--destructive)}.aria-invalid\:ring-destructive\/20[aria-invalid=true]{--tw-ring-color:color-mix(in oklab,var(--destructive)20%,transparent)}.data-\[active\=true\]\:z-10[data-active=true]{z-index:10}.data-\[active\=true\]\:border-ring[data-active=true]{border-color:var(--ring)}.data-\[active\=true\]\:ring-\[3px\][data-active=true]{--tw-ring-shadow:var(--tw-ring-inset,)0 0 0 calc(3px + var(--tw-ring-offset-width))var(--tw-ring-color,currentColor);box-shadow:var(--tw-inset-shadow),var(--tw-inset-ring-shadow),var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow)}.data-\[active\=true\]\:ring-ring\/50[data-active=true]{--tw-ring-color:color-mix(in oklab,var(--ring)50%,transparent)}.data-\[active\=true\]\:aria-invalid\:border-destructive[data-active=true][aria-invalid=true]{border-color:var(--destructive)}.data-\[active\=true\]\:aria-invalid\:ring-destructive\/20[data-active=true][aria-invalid=true]{--tw-ring-color:color-mix(in oklab,var(--destructive)20%,transparent)}.data-\[disabled\]\:pointer-events-none[data-disabled]{pointer-events:none}.data-\[disabled\]\:opacity-50[data-disabled]{opacity:.5}.data-\[error\=true\]\:text-destructive-foreground[data-error=true]{color:var(--destructive-foreground)}.data-\[inset\]\:pl-8[data-inset]{padding-left:calc(var(--spacing)*8)}.data-\[orientation\=horizontal\]\:h-px[data-orientation=horizontal]{height:1px}.data-\[orientation\=horizontal\]\:w-full[data-orientation=horizontal]{width:100%}.data-\[orientation\=vertical\]\:h-full[data-orientation=vertical]{height:100%}.data-\[orientation\=vertical\]\:w-px[data-orientation=vertical]{width:1px}.data-\[placeholder\]\:text-muted-foreground[data-placeholder]{color:var(--muted-foreground)}.data-\[side\=bottom\]\:translate-y-1[data-side=bottom]{--tw-translate-y:calc(var(--spacing)*1);translate:var(--tw-translate-x)var(--tw-translate-y)}.data-\[side\=bottom\]\:slide-in-from-top-2[data-side=bottom]{--tw-enter-translate-y:-8px}.data-\[side\=left\]\:-translate-x-1[data-side=left]{--tw-translate-x:calc(var(--spacing)*-1);translate:var(--tw-translate-x)var(--tw-translate-y)}.data-\[side\=left\]\:slide-in-from-right-2[data-side=left]{--tw-enter-translate-x:8px}.data-\[side\=right\]\:translate-x-1[data-side=right]{--tw-translate-x:calc(var(--spacing)*1);translate:var(--tw-translate-x)var(--tw-translate-y)}.data-\[side\=right\]\:slide-in-from-left-2[data-side=right]{--tw-enter-translate-x:-8px}.data-\[side\=top\]\:-translate-y-1[data-side=top]{--tw-translate-y:calc(var(--spacing)*-1);translate:var(--tw-translate-x)var(--tw-translate-y)}.data-\[side\=top\]\:slide-in-from-bottom-2[data-side=top]{--tw-enter-translate-y:8px}:is(.\*\:data-\[slot\=alert-description\]\:text-destructive-foreground\/80>*)[data-slot=alert-description]{color:color-mix(in oklab,var(--destructive-foreground)80%,transparent)}:is(.\*\:data-\[slot\=select-value\]\:line-clamp-1>*)[data-slot=select-value]{-webkit-line-clamp:1;-webkit-box-orient:vertical;display:-webkit-box;overflow:hidden}:is(.\*\:data-\[slot\=select-value\]\:flex>*)[data-slot=select-value]{display:flex}:is(.\*\:data-\[slot\=select-value\]\:items-center>*)[data-slot=select-value]{align-items:center}:is(.\*\:data-\[slot\=select-value\]\:gap-2>*)[data-slot=select-value]{gap:calc(var(--spacing)*2)}.data-\[state\=active\]\:bg-background[data-state=active]{background-color:var(--background)}.data-\[state\=active\]\:text-foreground[data-state=active]{color:var(--foreground)}.data-\[state\=active\]\:shadow-sm[data-state=active]{--tw-shadow:0 1px 3px 0 var(--tw-shadow-color,#0000001a),0 1px 2px -1px var(--tw-shadow-color,#0000001a);box-shadow:var(--tw-inset-shadow),var(--tw-inset-ring-shadow),var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow)}.data-\[state\=checked\]\:translate-x-4[data-state=checked]{--tw-translate-x:calc(var(--spacing)*4);translate:var(--tw-translate-x)var(--tw-translate-y)}.data-\[state\=checked\]\:border-primary[data-state=checked]{border-color:var(--primary)}.data-\[state\=checked\]\:bg-primary[data-state=checked]{background-color:var(--primary)}.data-\[state\=checked\]\:text-primary-foreground[data-state=checked]{color:var(--primary-foreground)}.data-\[state\=closed\]\:animate-accordion-up[data-state=closed]{animation:.2s ease-out accordion-up}.data-\[state\=closed\]\:animate-out[data-state=closed]{--tw-exit-opacity:initial;--tw-exit-scale:initial;--tw-exit-rotate:initial;--tw-exit-translate-x:initial;--tw-exit-translate-y:initial;animation-name:exit;animation-duration:.15s}.data-\[state\=closed\]\:fade-out-0[data-state=closed]{--tw-exit-opacity:0}.data-\[state\=closed\]\:zoom-out-95[data-state=closed]{--tw-exit-scale:.95}.data-\[state\=open\]\:animate-accordion-down[data-state=open]{animation:.2s ease-out accordion-down}.data-\[state\=open\]\:bg-accent[data-state=open]{background-color:var(--accent)}.data-\[state\=open\]\:text-accent-foreground[data-state=open]{color:var(--accent-foreground)}.data-\[state\=open\]\:text-muted-foreground[data-state=open]{color:var(--muted-foreground)}.data-\[state\=open\]\:animate-in[data-state=open]{--tw-enter-opacity:initial;--tw-enter-scale:initial;--tw-enter-rotate:initial;--tw-enter-translate-x:initial;--tw-enter-translate-y:initial;animation-name:enter;animation-duration:.15s}.data-\[state\=open\]\:fade-in-0[data-state=open]{--tw-enter-opacity:0}.data-\[state\=open\]\:zoom-in-95[data-state=open]{--tw-enter-scale:.95}.data-\[state\=selected\]\:bg-muted[data-state=selected]{background-color:var(--muted)}.data-\[state\=unchecked\]\:translate-x-0[data-state=unchecked]{--tw-translate-x:calc(var(--spacing)*0);translate:var(--tw-translate-x)var(--tw-translate-y)}.data-\[state\=unchecked\]\:bg-input[data-state=unchecked]{background-color:var(--input)}.data-\[variant\=destructive\]\:text-destructive-foreground[data-variant=destructive]{color:var(--destructive-foreground)}.data-\[variant\=destructive\]\:focus\:bg-destructive\/10[data-variant=destructive]:focus{background-color:color-mix(in oklab,var(--destructive)10%,transparent)}.data-\[variant\=destructive\]\:focus\:text-destructive-foreground[data-variant=destructive]:focus{color:var(--destructive-foreground)}@media (width>=40rem){.sm\:max-w-lg{max-width:var(--container-lg)}.sm\:flex-row{flex-direction:row}.sm\:justify-end{justify-content:flex-end}.sm\:text-left{text-align:left}}@media (width>=48rem){.md\:text-sm{font-size:var(--text-sm);line-height:var(--tw-leading,var(--text-sm--line-height))}}.dark\:focus-visible\:ring-destructive\/40:is(.dark *):focus-visible,.dark\:aria-invalid\:ring-destructive\/40:is(.dark *)[aria-invalid=true],.dark\:data-\[active\=true\]\:aria-invalid\:ring-destructive\/40:is(.dark *)[data-active=true][aria-invalid=true]{--tw-ring-color:color-mix(in oklab,var(--destructive)40%,transparent)}.dark\:data-\[variant\=destructive\]\:focus\:bg-destructive\/40:is(.dark *)[data-variant=destructive]:focus{background-color:color-mix(in oklab,var(--destructive)40%,transparent)}.\[\&_p\]\:leading-relaxed p{--tw-leading:var(--leading-relaxed);line-height:var(--leading-relaxed)}.\[\&_svg\]\:pointer-events-none svg{pointer-events:none}.\[\&_svg\]\:shrink-0 svg{flex-shrink:0}.\[\&_svg\:not\(\[class\*\=\'size-\'\]\)\]\:size-4 svg:not([class*=size-]){width:calc(var(--spacing)*4);height:calc(var(--spacing)*4)}.\[\&_svg\:not\(\[class\*\=\'text-\'\]\)\]\:text-muted-foreground svg:not([class*=text-]){color:var(--muted-foreground)}.\[\&_tr\]\:border-b tr{border-bottom-style:var(--tw-border-style);border-bottom-width:1px}.\[\&_tr\:last-child\]\:border-0 tr:last-child{border-style:var(--tw-border-style);border-width:0}.\[\&\:has\(\[role\=checkbox\]\)\]\:pr-0:has([role=checkbox]){padding-right:calc(var(--spacing)*0)}:is(.\*\:\[span\]\:last\:flex>*):is(span):last-child{display:flex}:is(.\*\:\[span\]\:last\:items-center>*):is(span):last-child{align-items:center}:is(.\*\:\[span\]\:last\:gap-2>*):is(span):last-child{gap:calc(var(--spacing)*2)}:is(.data-\[variant\=destructive\]\:\*\:\[svg\]\:\!text-destructive-foreground[data-variant=destructive]>*):is(svg){color:var(--destructive-foreground)!important}.\[\&\>\[role\=checkbox\]\]\:translate-y-\[2px\]>[role=checkbox]{--tw-translate-y:2px;translate:var(--tw-translate-x)var(--tw-translate-y)}.\[\&\>svg\]\:pointer-events-none>svg{pointer-events:none}.\[\&\>svg\]\:size-3>svg{width:calc(var(--spacing)*3);height:calc(var(--spacing)*3)}.\[\&\>svg\]\:size-4>svg{width:calc(var(--spacing)*4);height:calc(var(--spacing)*4)}.\[\&\>svg\]\:translate-y-0\.5>svg{--tw-translate-y:calc(var(--spacing)*.5);translate:var(--tw-translate-x)var(--tw-translate-y)}.\[\&\>svg\]\:text-current>svg{color:currentColor}.\[\&\>tr\]\:last\:border-b-0>tr:last-child{border-bottom-style:var(--tw-border-style);border-bottom-width:0}.\[\&\[data-state\=open\]\>svg\]\:rotate-180[data-state=open]>svg{rotate:180deg}@media (hover:hover){a.\[a\&\]\:hover\:bg-accent:hover{background-color:var(--accent)}a.\[a\&\]\:hover\:bg-destructive\/90:hover{background-color:color-mix(in oklab,var(--destructive)90%,transparent)}a.\[a\&\]\:hover\:bg-primary\/90:hover{background-color:color-mix(in oklab,var(--primary)90%,transparent)}a.\[a\&\]\:hover\:bg-secondary\/90:hover{background-color:color-mix(in oklab,var(--secondary)90%,transparent)}a.\[a\&\]\:hover\:text-accent-foreground:hover{color:var(--accent-foreground)}}}:host{--background:oklch(1 0 0);--foreground:oklch(.145 0 0);--card:oklch(1 0 0);--card-foreground:oklch(.145 0 0);--popover:oklch(1 0 0);--popover-foreground:oklch(.145 0 0);--primary:oklch(.205 0 0);--primary-foreground:oklch(.985 0 0);--secondary:oklch(.97 0 0);--secondary-foreground:oklch(.205 0 0);--muted:oklch(.97 0 0);--muted-foreground:oklch(.556 0 0);--accent:oklch(.97 0 0);--accent-foreground:oklch(.205 0 0);--destructive:oklch(.577 .245 27.325);--destructive-foreground:oklch(.577 .245 27.325);--border:oklch(.922 0 0);--input:oklch(.922 0 0);--ring:oklch(.708 0 0);--chart-1:oklch(.646 .222 41.116);--chart-2:oklch(.6 .118 184.704);--chart-3:oklch(.398 .07 227.392);--chart-4:oklch(.828 .189 84.429);--chart-5:oklch(.769 .188 70.08);--radius:10px;--sidebar:oklch(.985 0 0);--sidebar-foreground:oklch(.145 0 0);--sidebar-primary:oklch(.205 0 0);--sidebar-primary-foreground:oklch(.985 0 0);--sidebar-accent:oklch(.97 0 0);--sidebar-accent-foreground:oklch(.205 0 0);--sidebar-border:oklch(.922 0 0);--sidebar-ring:oklch(.708 0 0)}.dark{--background:oklch(.145 0 0);--foreground:oklch(.985 0 0);--card:oklch(.145 0 0);--card-foreground:oklch(.985 0 0);--popover:oklch(.145 0 0);--popover-foreground:oklch(.985 0 0);--primary:oklch(.985 0 0);--primary-foreground:oklch(.205 0 0);--secondary:oklch(.269 0 0);--secondary-foreground:oklch(.985 0 0);--muted:oklch(.269 0 0);--muted-foreground:oklch(.708 0 0);--accent:oklch(.269 0 0);--accent-foreground:oklch(.985 0 0);--destructive:oklch(.396 .141 25.723);--destructive-foreground:oklch(.637 .237 25.331);--border:oklch(.269 0 0);--input:oklch(.269 0 0);--ring:oklch(.556 0 0);--chart-1:oklch(.488 .243 264.376);--chart-2:oklch(.696 .17 162.48);--chart-3:oklch(.769 .188 70.08);--chart-4:oklch(.627 .265 303.9);--chart-5:oklch(.645 .246 16.439);--sidebar:oklch(.205 0 0);--sidebar-foreground:oklch(.985 0 0);--sidebar-primary:oklch(.488 .243 264.376);--sidebar-primary-foreground:oklch(.985 0 0);--sidebar-accent:oklch(.269 0 0);--sidebar-accent-foreground:oklch(.985 0 0);--sidebar-border:oklch(.269 0 0);--sidebar-ring:oklch(.439 0 0)}@keyframes enter{0%{opacity:var(--tw-enter-opacity,1);transform:translate3d(var(--tw-enter-translate-x,0),var(--tw-enter-translate-y,0),0)scale3d(var(--tw-enter-scale,1),var(--tw-enter-scale,1),var(--tw-enter-scale,1))rotate(var(--tw-enter-rotate,0))}}@keyframes exit{to{opacity:var(--tw-exit-opacity,1);transform:translate3d(var(--tw-exit-translate-x,0),var(--tw-exit-translate-y,0),0)scale3d(var(--tw-exit-scale,1),var(--tw-exit-scale,1),var(--tw-exit-scale,1))rotate(var(--tw-exit-rotate,0))}}@property --tw-translate-x{syntax:"*";inherits:false;initial-value:0}@property --tw-translate-y{syntax:"*";inherits:false;initial-value:0}@property --tw-translate-z{syntax:"*";inherits:false;initial-value:0}@property --tw-rotate-x{syntax:"*";inherits:false;initial-value:rotateX(0)}@property --tw-rotate-y{syntax:"*";inherits:false;initial-value:rotateY(0)}@property --tw-rotate-z{syntax:"*";inherits:false;initial-value:rotateZ(0)}@property --tw-skew-x{syntax:"*";inherits:false;initial-value:skewX(0)}@property --tw-skew-y{syntax:"*";inherits:false;initial-value:skewY(0)}@property --tw-space-y-reverse{syntax:"*";inherits:false;initial-value:0}@property --tw-space-x-reverse{syntax:"*";inherits:false;initial-value:0}@property --tw-border-style{syntax:"*";inherits:false;initial-value:solid}@property --tw-leading{syntax:"*";inherits:false}@property --tw-font-weight{syntax:"*";inherits:false}@property --tw-tracking{syntax:"*";inherits:false}@property --tw-shadow{syntax:"*";inherits:false;initial-value:0 0 #0000}@property --tw-shadow-color{syntax:"*";inherits:false}@property --tw-inset-shadow{syntax:"*";inherits:false;initial-value:0 0 #0000}@property --tw-inset-shadow-color{syntax:"*";inherits:false}@property --tw-ring-color{syntax:"*";inherits:false}@property --tw-ring-shadow{syntax:"*";inherits:false;initial-value:0 0 #0000}@property --tw-inset-ring-color{syntax:"*";inherits:false}@property --tw-inset-ring-shadow{syntax:"*";inherits:false;initial-value:0 0 #0000}@property --tw-ring-inset{syntax:"*";inherits:false}@property --tw-ring-offset-width{syntax:"<length>";inherits:false;initial-value:0}@property --tw-ring-offset-color{syntax:"*";inherits:false;initial-value:#fff}@property --tw-ring-offset-shadow{syntax:"*";inherits:false;initial-value:0 0 #0000}@property --tw-outline-style{syntax:"*";inherits:false;initial-value:solid}@property --tw-duration{syntax:"*";inherits:false}@property --tw-ease{syntax:"*";inherits:false}@property --tw-content{syntax:"*";inherits:false;initial-value:""}@keyframes spin{to{transform:rotate(360deg)}}@keyframes pulse{50%{opacity:.5}}@keyframes accordion-down{0%{height:0}to{height:var(--radix-accordion-content-height)}}@keyframes accordion-up{0%{height:var(--radix-accordion-content-height)}to{height:0}}@keyframes caret-blink{0%,70%,to{opacity:1}20%,50%{opacity:0}}</style></head><body><div></div></body></html></template></browser-mcp-container></body></html>