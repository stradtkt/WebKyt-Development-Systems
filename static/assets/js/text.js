$(function() {
    $('.services-tlt-h1').textillate({
        loop: true,
        minDisplayTime: 2000,
        initialDelay: 0,
        inEffects: [],
        outEffects: ['hinge'],
        in: {
            effect: 'fadeInLeftBig',
            delayScale: 1.5,
            delay: 50,
            sync: false,
            shuffle: false,
            reverse: true,
            callback: function() {}
        },
        out: {
            effect: 'hinge',
            delayScale: .5,
            delay: 50,
            sync: false,
            shuffle: false,
            reverse: false,
            callback: function() {}
        },
        callback: function() {},
        type: 'char'
    });
    $('.services-tlt-p').textillate({
        loop: true,
        minDisplayTime: 875,
        initialDelay: 0,
        inEffects: [],
        outEffects: ['hinge'],
        in: {
            effect: 'fadeInRightBig',
            delayScale: 1.5,
            delay: 50,
            sync: false,
            shuffle: false,
            reverse: true,
            callback: function() {}
        },
        out: {
            effect: 'hinge',
            delayScale: .5,
            delay: 50,
            sync: false,
            shuffle: false,
            reverse: false,
            callback: function() {}
        },
        callback: function() {},
        type: 'char'
    });
    $(".home-tlt-h1").textillate({
        loop: false,
        minDisplayTime: 2000,
        initialDelay: 0,
        inEffects: [],
        outEffects: ['bounceOutUp'],
        in: {
            effect: 'flip',
            delayScale: 1.5,
            delay: 50,
            sync: false,
            shuffle: false,
            reverse: false,
            callback: function() {}
        },
        out: {
            effect: 'bounceOutUp',
            delayScale: 1.5,
            delay: 50,
            sync: true,
            shuffle: false,
            reverse: false,
            callback: function() {}
        },
        callback: function() {},
        type: 'char'
    });
    $(".home-tlt-p").textillate({
        loop: false,
        minDisplayTime: 2000,
        initialDelay: 0,
        inEffects: [],
        outEffects: ['bounceOutDown'],
        in: {
            effect: 'flip',
            delayScale: 1.5,
            delay: 50,
            sync: false,
            shuffle: false,
            reverse: false,
            callback: function() {}
        },
        out: {
            effect: 'bounceOutDown',
            delayScale: 1.5,
            delay: 100,
            sync: true,
            shuffle: false,
            reverse: false,
            callback: function() {}
        },
        callback: function() {},
        type: 'char'
    });
});