.. title: Search
.. slug: search
.. date: 2015-11-25 07:05:36 UTC
.. tags: search
.. category:
.. link:
.. description:
.. type: text

Use the form below to perform a search on the whole website.

.. raw:: html

    <form method="get"
        action="https://www.google.com/search"
        id="search-form"
        class="form-inline"
        role="search">
        <div class="form-group">
            <input
                type="text"
                name="q"
                class="form-control"
                placeholder="Search">
            <button type="submit" class="btn btn-primary">
                <span class="fas fa-search"></span>
            </button>
        </div>
        <input
            type="hidden"
            name="sitesearch"
            value="http://colour-science.org/">
    </form>
    <div class="mt-5"></div>