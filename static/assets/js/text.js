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
});