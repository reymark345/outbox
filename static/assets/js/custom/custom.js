var kanban2 = new jKanban({
  element: '#demo2',
  gutter:'15px',
  buttonClick  : function (el, boardId) {
    alert(el.innerHTML);
  },
  boards: [{
    'id': '0',
    'title': 'To do',
    'class': 'bg-info',
    'dragTo': ['1'],
    'item': [
      {% for tasking in requestsdata %}
    {
      'title': `
            <a class="kanban-box" href="#" data-id="{{tasking.id}}"><span class="date" >{{tasking.date_requested}}</span><span class="badge badge-info f-right">medium</span>
              <h6>{{tasking.title}}</h6>
              <div class="media"><img class="img-20 me-1 rounded-circle" src="/static/assets/images/user/3.jpg" alt="" data-original-title="" title="">
                <div class="media-body">
                  <p>{{tasking.description|truncatechars:200}}</p>
                  <p class="f-12">Requested by: <b>Reymark N. Valdehueza</b></p>
                </div>
              </div>
              <div class="d-flex mt-3">
                <ul class="list">
                  <li><i class="fa fa-comments-o"></i>2</li>
                  <li><i class="fa fa-paperclip"></i>2</li>
                  <li><i class="fa fa-eye"></i></i></li>
                </ul>
                <div class="customers">
                  <ul>
                    <li class="d-inline-block me-3">
                      
                    </li>
                    <li class="d-inline-block"><img class="img-20 rounded-circle" src="/static/assets/images/user/1.jpg" alt="" data-original-title="" title=""></li>
                  </ul>
                </div>
              </div></a>
        `,
      },{% endfor %}
    ]
  },
{
  'id': '1',
    'title': 'In Progress',
      'class': 'bg-warning',
        'dragTo': ['0','2'],
          'item': [
          {% for tasking in requestsdata %} 
          {
            'title': `
                  <a class="kanban-box" href="#" data-id="{{tasking.id}}"><span class="date" >{{tasking.date_requested}}</span><span class="badge badge-danger f-right">Argent</span>
                    <h6>{{tasking.title}}</h6>
                    <div class="media"><img class="img-20 me-1 rounded-circle" src="/static/assets/images/user/3.jpg" alt="" data-original-title="" title="">
                      <div class="media-body">
                        <p>{{tasking.description|truncatechars:200}}</p>
                        <p class="f-12">Requested by: <b>Reymark N. Valdehueza</b></p>
                      </div>
                    </div>
                    <div class="d-flex mt-3">
                      <ul class="list">
                        <li><i class="fa fa-comments-o"></i>2</li>
                        <li><i class="fa fa-paperclip"></i>2</li>
                        <li><i class="fa fa-eye"></i></i></li>
                      </ul>
                      <div class="customers">
                        <ul>
                          <li class="d-inline-block me-3">
                            <p class="f-12">+5</p>
                          </li>
                          <li class="d-inline-block"><img class="img-20 rounded-circle" src="/static/assets/images/user/1.jpg" alt="" data-original-title="" title=""></li> 
                        </ul>
                      </div>
                    </div></a>
                `,
          },{% endfor %}
          ]
},
{
  'id': '2',
    'title': 'Review',
      'class': 'bg-danger',
        'dragTo': ['1','3'],
          'item': [
          {% for tasking in requestsdata %}
          {
            'title': `
                  <a class="kanban-box" href="#" data-id="{{tasking.id}}"><span class="date" >{{tasking.date_requested}}</span><span class="badge badge-success f-right">Low</span>
                    <h6>{{tasking.title}}</h6>
                    <div class="media"><img class="img-20 me-1 rounded-circle" src="/static/assets/images/user/3.jpg" alt="" data-original-title="" title="">
                      <div class="media-body">
                        <p>{{tasking.description|truncatechars:200}}</p>
                        <p class="f-12">Requested by: <b>Reymark N. Valdehueza</b></p>
                      </div>
                    </div>
                    <div class="d-flex mt-3">
                      <ul class="list">
                        <li><i class="fa fa-comments-o"></i>2</li>
                        <li><i class="fa fa-paperclip"></i>2</li>
                        <li><i class="fa fa-eye"></i></i></li>
                      </ul>
                      <div class="customers">
                        <ul>
                          <li class="d-inline-block me-3">
                            <p class="f-12">+5</p>
                          </li>
                          <li class="d-inline-block"><img class="img-20 rounded-circle" src="/static/assets/images/user/1.jpg" alt="" data-original-title="" title=""></li> 
                        </ul>
                      </div>
                    </div></a>
                `,
          },{% endfor %}
          ]
},
{
  'id': '3',
    'title': 'Done',
      'class': 'bg-success',
        'dragTo': ['2'],
          'item': [
          {% for tasking in requestsdata %}
          {
            'title': `
                <a class="kanban-box" href="#" data-id="{{tasking.id}}"><span class="date" >{{tasking.date_requested}}</span><span class="badge badge-danger f-right">Argent</span>
                  <h6>{{tasking.title}}</h6>
                  <div class="media"><img class="img-20 me-1 rounded-circle" src="/static/assets/images/user/3.jpg" alt="" data-original-title="" title="">
                    <div class="media-body">
                      <p>{{tasking.description|truncatechars:200}}</p>
                      <p class="f-12">Requested by: <b>Reymark N. Valdehueza</b></p>
                    </div>
                  </div>
                  <div class="d-flex mt-3">
                    <ul class="list">
                      <li><i class="fa fa-comments-o"></i>2</li>
                      <li><i class="fa fa-paperclip"></i>2</li>
                      <li><i class="fa fa-eye"></i></i></li>
                    </ul>
                    <div class="customers">
                      <ul>
                        <li class="d-inline-block me-3">
                          <p class="f-12">+5</p>
                        </li>
                        <li class="d-inline-block"><img class="img-20 rounded-circle" src="/static/assets/images/user/3.jpg" alt="" data-original-title="" title=""></li>
                        <li class="d-inline-block"><img class="img-20 rounded-circle" src="/static/assets/images/user/1.jpg" alt="" data-original-title="" title=""></li>
                        <li class="d-inline-block"><img class="img-20 rounded-circle" src="/static/assets/images/user/5.jpg" alt="" data-original-title="" title=""></li>
                      </ul>
                    </div>
                  </div></a>
            `,
          },{% endfor %}
          ]
}],
dropEl: function (el, target, source, sibling) {

}});