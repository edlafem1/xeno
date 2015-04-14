<header id="header">
    <br/>
    <div id="header_container">
        <section class="header_group">
            <table>
                <tr class="fadeInDown">
                    <td><a href="/search" class="header_link">XENO</a></td>

                    {% if admin %}
<!--                <td><a href="/add" class="header_link">ADD CAR</a></td>-->
                    <td><a href="/accounts" class="header_link">ACCOUNTS</a></td>
<!--                    <td><a href="#" class="header_link">LOG</a></td>-->
                    <td><a href="/addcar" class="header_link">ADD CAR</a></td>
                    {% else %}
                    <td><a href="/dashboard" class="header_link">DASHBOARD</a></td>
                    {% endif %}
                    <td><input type="roundedTextbox" placeholder="Search"/></td>
                    {% if admin %}
                    <td><a href="/dashboard" class="header_link">DASHBOARD</a></td>
                    {% endif %}
                    <td><a href="/profile" class="header_link">PROFILE</a></td>
                    <td><a href="{{ url_for('logout') or '#' }}" class="header_link">LOGOUT</a></td>
                </tr>
            </table>
        </section>
    </div>
</header>