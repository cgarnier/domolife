<?php

namespace Domolife\EnoceanBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\RedirectResponse;

class FrontendController extends Controller
{
    public function indexAction()
    {
        return new Response('Hello', 200);
    }
}
