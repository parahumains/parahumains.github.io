;(function() {
    var footnotes = document.querySelectorAll('.footnotes p');

    for (var i = 0; i < footnotes.length; i++) {
        var footnote = footnotes[i];
        var noteText = footnote.childNodes[0].textContent;

        var refId = 'fnref:' + (i + 1).toString();
        var ref = document.getElementById(refId);

        ref.textContent = '†';
        ref.setAttribute('data-hover', noteText);

        // add a div as the parent to the † and the hover text
        var parent = ref.parentNode;
        var wrapper = document.createElement('div');
        wrapper.classList.add('footnote');

        parent.replaceChild(wrapper, ref);
        wrapper.appendChild(ref);

        var hoverText = document.createElement('div');
        hoverText.textContent = noteText;
        wrapper.appendChild(hoverText);
    }

    document.querySelector('.footnotes').outerHTML = '';
}
)();
